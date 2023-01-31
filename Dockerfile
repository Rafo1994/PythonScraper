FROM ubuntu:20.04

WORKDIR /app

RUN apt-get update && apt-get -y install cron && apt-get -y install python3 && apt-get -y install python3-pip && apt-get -y install libpq-dev && apt-get -y install python3-dev && apt-get -y install nano


COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY  * ./

RUN python3 CreateCron.py

RUN chmod 0644 /etc/cron.d/crontab
RUN chmod +x /app/entry.sh
RUN chmod +x /app/cron-script.sh
RUN /usr/bin/crontab /etc/cron.d/crontab

#RUN printenv | grep 'DB_HOST' >> /etc/environment
# run crond as main process of container
CMD ["/app/entry.sh"]
