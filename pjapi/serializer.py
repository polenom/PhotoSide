from rest_framework import serializers
from photojournal.models import *

class BlogsSerializer(serializers.ModelSerializer):
    # user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Blog
        fields = '__all__'
        read_only_fields = ['likesBlog','user']
#     def create(self, validated_data):
#         return Blog.objects.create(**validated_data)

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
#
#
# class BlogUpdateSerializer(serializers.Serializer):
#     title = serializers.CharField()
#     # photo = serializers.ImageField()
#     slug = serializers.SlugField()
#     description = serializers.CharField()
#
#     def update(self, instance, validated_data):
#         print(validated_data, 'start')
#         # instance.photo = invalidated_data.get("photo", instance.photo)
#         instance.description = validated_data.get("description", instance.description)
#         # instance.title = validated_data.get("title", instance.title)
#         instance.slug = validated_data.get("slug", instance.slug)
#         print(instance.description, 'finish')
#         instance.save()
#         return instance

    # user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Имя пользователя', related_name='blogs')
    # photo = models.ImageField(upload_to=photo_path, verbose_name='Фото')
    # description = models.TextField(max_length=100, verbose_name='Описание')
    # creation = models.DateTimeField(auto_now=True, verbose_name='Дата создания')
    # photoPublish = models.BooleanField(default=True, verbose_name='Статус')
    # likesBlog = models.ManyToManyField(User, blank=True, related_name='likes')
    # title = models.CharField(max_length=40, unique=True)
    # slug = models.SlugField(null=True)