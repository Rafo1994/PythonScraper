FROM ubuntu:jammy-20221130

WORKDIR /app

RUN apt-get update && apt-get -y install cron && apt-get -y install python3 && apt-get -y install python3-pip && apt-get -y install libpq-dev && apt-get -y install python3-dev

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY  * ./

RUN python3 CreateCron.py

# Give execution rights on the cron job
RUN chmod 0644 cron-job

# Apply cron job
RUN crontab cron-job

# Create the log file to be able to run tail
RUN touch /var/log/cron.log

# Run the command on container startup
CMD cron && tail -f /var/log/cron.log
