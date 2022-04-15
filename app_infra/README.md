# Applications' service modules

docker build -f Dockerfile_db_create_tables -t create_db:1 .<br>
docker build -f Dockerfile_db_drop_tables -t drop_db:1 .<br><br>

<b>create_db</b> is the service application for creating database schema.<br>
<b>drop_db</b> is the service application for deleting database schema.<br>
