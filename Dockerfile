FROM ubuntu:18.04

ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /app

RUN pip3 install -r requirements.txt

CMD ["python3", "bot.py"]

