from rest_framework import serializers
from photojournal.models import *

class BlogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('photo', 'description', 'creation', 'user')

