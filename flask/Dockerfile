FROM alpine:3.7

LABEL maintainer="Jordi Jaspers"

RUN apk add --no-cache python3-dev \
          && pip3 install --upgrade pip

RUN apk update

RUN apk add make automake gcc g++ subversion python3-dev          

ADD . /code

WORKDIR /code

RUN \
 apk add --no-cache python3 postgresql-libs && \
 apk add --no-cache --virtual .build-deps gcc python3-dev musl-dev postgresql-dev && \
 python3 -m pip install -r requirements.txt --no-cache-dir && \
 apk --purge del .build-deps

EXPOSE 5000

CMD ["python3", "app.py"]

