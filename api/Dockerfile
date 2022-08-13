FROM python:3.8-slim-buster

COPY ./api ./app
WORKDIR /app
RUN pip install -r ./requirements.txt
ENTRYPOINT [ "python" ]
CMD ["app.py"]