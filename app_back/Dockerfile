FROM python:3.9-slim
WORKDIR /app
COPY . .
RUN pip install psycopg2-binary && pip3 install -r requirements.txt
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]