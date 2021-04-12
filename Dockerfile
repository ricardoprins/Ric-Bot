FROM python:3.8.9-slim-buster

WORKDIR /usr/src/app

COPY . .

RUN pip install pipenv

RUN pipenv install

CMD ["pipenv","run","python","./src/main.py"]