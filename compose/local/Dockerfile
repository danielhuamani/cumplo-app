FROM python:3.6-alpine
RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add --repository http://dl-cdn.alpinelinux.org/alpine/edge/main \
    libcrypto1.1 \
    && apk add --repository http://dl-cdn.alpinelinux.org/alpine/edge/testing \
    gdal-dev \
    geos-dev \
    && apk add postgresql \
    && apk add postgresql-dev \
    && apk add jpeg-dev zlib-dev libjpeg \
    && apk add musl-dev jpeg-dev mysql-dev \
    && pip install mysqlclient
ENV PYTHONUNBUFFERED=1
RUN mkdir /code
WORKDIR /code
COPY ./requirements/ ./requirements
RUN pip install -r ./requirements/local.txt
COPY ./compose/local/docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh
RUN ls
ENTRYPOINT ["/docker-entrypoint.sh"]
EXPOSE 8000

