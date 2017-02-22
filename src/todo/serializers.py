from rest_framework import serializers
from todo.models import TodoItem

class TodoItemSerializer(serializers.HyperlinkedModelSerializer):
	"""docstring for TodoItemSerializer"""

	url = serializers.ReadOnlyField()
	class Meta:
		"""docstring for Meta"""
		model = TodoItem
		fields = ('url','title','completed','order')	