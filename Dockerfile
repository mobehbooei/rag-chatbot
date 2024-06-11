FROM ubuntu:22.04

WORKDIR /app

COPY requirements.txt .

RUN apt-get update && \
    apt-get install -y python3 python3-venv python3-pip && \
    rm -rf /var/lib/apt/lists/*

RUN python3 -m venv venv
RUN /bin/bash -c "source venv/bin/activate"

RUN pip install --no-cache-dir -r requirements.txt

COPY ./.env .
COPY ./app /app

ENV FLASK_APP=routes
ENV FLASK_ENV=development

EXPOSE 5000

CMD ["flask", "run", "--host", "0.0.0.0"]