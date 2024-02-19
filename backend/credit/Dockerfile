FROM python:3.12.2

ENV PYTHONUNBUFFERED = 1

RUN pip install - r requirements.txt

WORKDIR /backend

EXPOSE 8000

CMD [ "python" , "manage.py" , "runserver" ]