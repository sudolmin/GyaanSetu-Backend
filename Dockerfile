FROM python:3.11.8-slim-bookworm

RUN apt update
RUN pip install --upgrade pip
RUN apt-get install curl libsm6 libxext6 libpq-dev \
    cmake nano gcc poppler-utils -y

COPY ./GyaanSetu/requirements.txt .
RUN pip install -r requirements.txt

COPY ./GyaanSetu /app

WORKDIR /app

COPY ./entrypoint.sh /

ENTRYPOINT ["sh", "/entrypoint.sh"]