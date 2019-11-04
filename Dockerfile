FROM python:3.7

WORKDIR /app
COPY . .

ENV GOOGLE_APPLICATION_CREDENTIALS=google-credentials.json

RUN pip install pipenv
RUN pipenv install --system --deploy

ENV PORT=5000

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --limit-request-line 10000 app:app