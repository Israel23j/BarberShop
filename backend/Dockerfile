FROM python:3.10-slim

ENV APP_HOME=/app
WORKDIR ${APP_HOME}

COPY . .

RUN pip install -r requirements.txt

CMD [ "uvicorn", "main:app", "--host", "0.0.0.0" ,"--port" ,"80", "--reload" ]
