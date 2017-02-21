from rest_framework import serializers
from todo.models import TodoItem

class TodoItemSerializer(serializers.HyperlinkedModel):
	"""docstring for TodoItemSerializer"""
	def __init__(self, arg):
		super(TodoItemSerializer, self).__init__()
		self.arg = arg
	url = serializers.ReadOnlyField()
	class Meta:
		"""docstring for Meta"""
		model = TodoItem
		fields = ('url','title','completed','order')	