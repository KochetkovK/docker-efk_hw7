FROM python:3-alpine
RUN mkdir /app
WORKDIR /app
ADD requirements.txt /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ADD . /app
EXPOSE 5000
ENTRYPOINT ["gunicorn","--bind","0.0.0.0:5000","--log-config","log_4.conf","wsgi:app"]