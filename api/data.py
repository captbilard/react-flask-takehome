
from app import db, Company, User, Client

db.create_all()

companyXYZ = Company(name='Company XYZ')
companyABC = Company(name='Company ABC')
companyAMZ = Company(name='Company AMZ')

user1 = User(name='John Doe', email_address="john.doe@companyxyz.com",
             availability_status='available', company=companyXYZ)

user2 = User(name='Mary Mapt', email_address="mary.mapt@companyxyz.com",
             availability_status='not available', company=companyXYZ)

user3 = User(name='Cindy Smith', email_address="cindy.smith@companyabc.com",
             availability_status='available', company=companyABC)

user4 = User(name='Alison Danny', email_address="alison.danny@companyabc.com",
             availability_status='not available', company=companyABC)

user5 = User(name='Harry Potter', email_address="harry.potter@companyamz.com",
             availability_status='available', company=companyAMZ)

user6 = User(name='Taylor Pitcher', email_address="taylor.pitcher@companyamz.com",
             availability_status='not available', company=companyAMZ)

client1 = Client(name='Client 1', email_address="client1@email.com")
client2 = Client(name='Client 2', email_address="client2@email.com")

db.session.add(user1)
db.session.add(user2)
db.session.add(user3)
db.session.add(user4)
db.session.add(user5)
db.session.add(user6)
db.session.add(client1)
db.session.add(client2)

db.session.commit()
