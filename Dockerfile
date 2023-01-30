FROM alpine:3.17.1

WORKDIR /app

ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN apk add --no-cache python3 py3-pip libpq-dev
RUN apk add --no-cache apk-cron
RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools

RUN \
 apk add --no-cache postgresql-libs && \
 apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
 apk --purge del .build-deps

#RUN apt-get update && apt-get -y install cron && apt-get -y install python3 && apt-get -y install python3-pip && apt-get -y install libpq-dev && apt-get -y install python3-dev

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY  * ./

RUN python3 CreateCron.py

# Give execution rights on the cron job
RUN chmod 755 cron-job

RUN /usr/bin/crontab cron-job
# Apply cron job
RUN chmod 755 entry.sh

CMD ["/app/entry.sh"]
