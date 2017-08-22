FROM python:2.7-alpine3.6
MAINTAINER Derek Wene (dwene)
WORKDIR /app/
COPY . /app/
RUN pip install requests
RUN apk add --no-cache tini
ENTRYPOINT ["python", "evacuate.py"]