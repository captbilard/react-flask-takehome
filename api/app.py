from sqlalchemy_utils import ChoiceType
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc
from flask import Flask, request
from flask_restx import Resource, fields, Api
from flask_cors import CORS, cross_origin
from flask_mail import Mail, Message
from tasks import make_celery


app = Flask(__name__)
api = Api(app)

CORS(app, resources={r"*": {"origins": "*"}})
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config.update(
    CELERY_CONFIG={
        "broker_url": "amqps://ossstawe:aAKgWlYDCXH6mKFgua1P2CX3sMsoTo_b@chimpanzee.rmq.cloudamqp.com/ossstawe"
    }
)
db = SQLAlchemy(app)
celery = make_celery(app)
TYPES = [("available", "Available"), ("not available", "Not available")]

########### Mail Configuration #############
app.config["MAIL_SERVER"] = "smtp.mailtrap.io"
app.config["MAIL_PORT"] = 2525
app.config["MAIL_USERNAME"] = "d6d7107d519e99"
app.config["MAIL_PASSWORD"] = "b5a41009a143bb"
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USE_SSL"] = False
mail = Mail(app)

########### Mail function #############
@celery.task
def send_client_mail(cleaner_name, client_email):
    msg = Message(
        "Cleaner Booking Confirmation",
        sender="company-yola@mailtrap.io",
        recipients=[client_email],
    )
    msg.body = f"Your booking for {cleaner_name} has been completed successfully"
    mail.send(msg)
    return "message sent"


@celery.task
def send_cleaner_mail(cleaner_email, cleaner_name, date_range):
    msg = Message(
        "Schedule Notification",
        sender="company-yola@mailtrap.io",
        recipients=[cleaner_email],
    )
    msg.body = f"Dear {cleaner_name}, You have been scheduled for a cleaning service dated {date_range}"
    mail.send(msg)
    return "message sent"


########### MODELS #############
class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    email_address = db.Column(db.String(120), unique=True, nullable=False)
    availability_status = db.Column(ChoiceType(TYPES), nullable=False)
    company_id = db.Column(db.Integer, db.ForeignKey("company.id"), nullable=False)
    company = db.relationship("Company", backref=db.backref("company", lazy=True))

    def __repr__(self):
        return "<User %r>" % self.name


class Schedule(db.Model):
    __tablename__ = "schedule"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    user = db.relationship("User", backref=db.backref("user", lazy=True))
    client_id = db.Column(db.Integer, db.ForeignKey("client.id"), nullable=False)
    client = db.relationship("Client", backref=db.backref("client", lazy=True))
    date_range = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return "<Schedule %r>" % self.id


class Company(db.Model):
    __tablename__ = "company"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return "<Schedule %r>" % self.id


class Client(db.Model):
    __tablename__ = "client"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    email_address = db.Column(db.String(120), unique=True, nullable=False)

    def _repr__(self):
        return "<Client %r>" % self.name


# ########### SERIALIZERS #############
company_serializer = api.model(
    "Model",
    {
        "id": fields.Integer(
            readOnly=True, description="The unique identifier of a company"
        ),
        "name": fields.String(required=True, description="The name of the company"),
    },
)

user_serializer = api.model(
    "Model",
    {
        "id": fields.Integer(
            readOnly=True, description="The unique identifier of user"
        ),
        "name": fields.String(required=True, description="The name of user"),
        "email_address": fields.String(
            required=True, description="The email address of user"
        ),
        "availability_status": fields.String(
            required=True, description="The availability status of user"
        ),
        "company": fields.Nested(company_serializer),
    },
)

client_serializer = api.model(
    "Model",
    {
        "email_address": fields.String(
            required=True, description="The email address of the client"
        )
    },
)

schedule_serializer = api.model(
    "Model",
    {
        "id": fields.Integer(
            readOnly=True, description="The unique identifier of a schedule"
        ),
        "user": fields.Nested(user_serializer),
        "client": fields.Nested(client_serializer),
        "date_range": fields.String(
            required=True, description="The date and time of the schedule"
        ),
    },
)

# ########### ROUTES #############
@api.route("/hello")
class HelloWorld(Resource):
    def get(self):
        return {"hello": "world"}


@api.route("/companies")
class Companies(Resource):
    @api.marshal_with(company_serializer, envelope="resource")
    def get(self):
        return Company.query.all()


@api.route("/users/<int:company_id>")
class Users(Resource):
    @api.marshal_with(user_serializer, envelope="resource")
    def get(self, company_id):
        return User.query.filter_by(company_id=company_id).all()


@api.route("/schedule")
class Schedules(Resource):
    @api.marshal_with(schedule_serializer, envelope="resource")
    def post(self):
        data = request.get_json()

        user_id = data.get("user")
        client_email = data.get("client_email")
        date = data.get("date")
        start_time = data.get("start_time")
        end_time = data.get("end_time")

        user = User.query.filter_by(id=user_id).first()
        client = Client.query.filter_by(email_address=client_email).first()
        date_range = f"{date} {start_time} to {date} {end_time}"

        try:
            new_Schedule = Schedule(user=user, client=client, date_range=date_range)
            db.session.add(new_Schedule)
            db.session.commit()
        except exc.IntegrityError:
            db.session.rollback()
            return "Internal server error"

        send_client_mail.delay(
            cleaner_name=user.name, client_email=client.email_address
        )
        send_cleaner_mail.delay(
            cleaner_email=user.email_address,
            cleaner_name=user.name,
            date_range=date_range,
        )

        print("Schedule successfully created")

        return new_Schedule
