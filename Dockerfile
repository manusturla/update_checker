FROM python:3.10.6
RUN apt-get update -y


EXPOSE 8080

COPY requirements.txt /
RUN pip3 install -r /requirements.txt
COPY . /app


#RUN chmod +x /app/wait-for-it.sh
RUN chmod +x /app/start_app.sh

WORKDIR /app
#ENTRYPOINT ["/app/wait-for-it.sh", "localhost:3306", "--", "/app/start_app.sh"]
ENTRYPOINT ["/app/start_app.sh"]