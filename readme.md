Terminal commands run to setup

	virtualenv venv
	source venv/bin/activate
	pip install ansible awscli boto boto3
	docker-machine create --driver virtualbox docker01
	docker-machine start docker01
	docker-machine env docker01
	eval $(docker-machine env docker01)

Useful URLs

	http://www.todobackend.com/
	http://www.django-rest-framework.org/api-guide/serializers/
	http://www.django-rest-framework.org/api-guide/views/


Django App commands
python manage.py startapp todo
python manage.py migrate
python manage.py test
python manage.py runserver
python manage.py test --settings=todobackend.settings.test

MySQL commands
mysql_secure_installation
mysql.server start
mysql -u root -p
GRANT ALL PRIVILEGES ON test_todobackend.* TO 'todo'@'localhost' identified by 'password';
GRANT ALL PRIVILEGES ON todobackend.* TO 'todo'@'localhost' identified by 'password';