terminal commands run to setup
	virtualenv venv
	source venv/bin/activate
	pip install ansible awscli boto boto3
	docker-machine create --driver virtualbox docker01
	docker-machine env docker01
	eval $(docker-machine env docker01)

Usefule URLs
http://www.todobackend.com/
http://www.django-rest-framework.org/api-guide/serializers/
http://www.django-rest-framework.org/api-guide/views/