# Flask project boilerplate

Contains a working boilerplate code for your Flask project:


- Integrated [Celery](http://celeryproject.org/) background tasks management

## How to start

```sh
$ mkdir Project
$ cd Project
$ git clone git@github.com:10hourlabs/python-flask-takehome.git
$ cd python-flask-takehome/api
$ pip install -r requirements.txt
$ make db
$ make dev
```
- _make db_ : populate database with dummy data
- _make dev_ : run development server


Open http://127.0.0.1:4000/, customize project files and **have fun**.

## Requirements

If you never worked with python projects then the simplest way is run project inside Docker. Follow instruction [how to install Docker in your OS](https://docs.docker.com/installation/).

## Included modules support

- [`Flask`](http://flask.pocoo.org/) & [`Werkzeug`](http://werkzeug.pocoo.org/) — base for everything.
- [`flask-restx`](https://flask-restx.readthedocs.io/) — restful API generator.
- [`Flask-SQLAlchemy`](https://flask-sqlalchemy.palletsprojects.com/) — database ORM layer build on top of SQLAlchemy, best python ORM with depth and flexibility.
- [`Celery`](http://celeryproject.org/) — background and deferred tasks broker.

## Project structure

    ├── app.py
    ├── README.md
    ├── .python-version
    ├── Dockerfile
    ├── requirements.txt
    ├── tasks.py
    ├── Makefile
