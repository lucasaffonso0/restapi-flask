FROM python:3.13.0a1-alpine3.18

EXPOSE 5000

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY application application

COPY wsgi.py config.py ./

CMD [ "python", "wsgi.py" ]