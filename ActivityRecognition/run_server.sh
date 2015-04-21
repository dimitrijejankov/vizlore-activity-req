rm -f /var/lib/mongodb/mongod.lock
mongod -repair 
service mongodb start
python manage.py runserver 0.0.0.0:8089