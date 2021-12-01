#!/bin/sh
echo "Starting server"

#!/bin/sh

while ! nc -z db 3306 ; do
    echo "Waiting for the MySQL Server"
    sleep 3
done

exec "$@"

python ./src/manage.py runserver 0.0.0.0:8000 --settings=config.settings.local