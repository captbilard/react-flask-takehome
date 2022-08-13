
from celery import Celery

# update to your own broker uri (rabbitMQ)
app = Celery('hello', broker='amqp://guest@localhost//')

# Run your background tasks here.


@app.task
def hello():
    return 'hello world'
