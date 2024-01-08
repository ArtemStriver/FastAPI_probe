FROM python:3.12

RUN mkdir /fast_api

WORKDIR /fast_api

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

#RUN alembic upgrade head

RUN chmod a+x docker/*.sh

#WORKDIR src

#CMD gunicorn src.main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000