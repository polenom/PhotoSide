from rest_framework import serializers
from photojournal.models import *

class BlogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('photo', 'description', 'creation', 'user', 'title','slug')


    def create(self, validated_data):

        return Blog.objects.create(**validated_data)