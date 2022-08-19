FROM python:3.10-slim-buster

COPY ./api ./app
WORKDIR /app
RUN pip install -r requirements.txt
RUN python data.py
EXPOSE 3001
CMD ["python", "runserver.py"]