FROM python:3.12.0

EXPOSE 5000

WORKDIR /app

RUN pip install flask[async] flask-cors requests asyncio urllib3

COPY . .

CMD python anime.py
