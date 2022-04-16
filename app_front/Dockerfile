FROM python:3.9-alpine
WORKDIR /app
COPY . .
RUN pip install psycopg2-binary && pip3 install -r requirements.txt
EXPOSE 5000
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]