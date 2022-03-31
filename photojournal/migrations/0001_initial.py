# Generated by Django 4.0.2 on 2022-03-28 18:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import photojournal.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to=photojournal.models.photo_path, verbose_name='Фото')),
                ('description', models.TextField(max_length=100, verbose_name='Описание')),
                ('creation', models.DateTimeField(auto_now=True, verbose_name='Дата создания')),
                ('photoPublish', models.BooleanField(default=True, verbose_name='Статус')),
                ('title', models.CharField(max_length=40, unique=True)),
                ('slug', models.SlugField(null=True)),
                ('likesBlog', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blogs', to=settings.AUTH_USER_MODEL, verbose_name='Имя пользователя')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userPhoto', models.FileField(blank=True, default='', null=True, upload_to=photojournal.models.user_path, verbose_name='Фото')),
                ('firstName', models.CharField(blank=True, default='', max_length=30, null=True, verbose_name='Имя')),
                ('secondName', models.CharField(blank=True, default='', max_length=30, null=True, verbose_name='Фамилия')),
                ('dateBirthday', models.DateTimeField(blank=True, null=True, verbose_name='День рождения')),
                ('emailProfile', models.EmailField(max_length=200, null=True, verbose_name='Почта')),
                ('slug', models.SlugField(null=True)),
                ('sub', models.ManyToManyField(blank=True, related_name='sub', to=settings.AUTH_USER_MODEL)),
                ('userProfile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL, verbose_name='')),
            ],
            options={
                'verbose_name': 'Профиль',
                'verbose_name_plural': 'Профиля',
            },
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=100, verbose_name='Коментарий')),
                ('creation', models.DateTimeField(auto_now=True, verbose_name='Дата создания')),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photojournal.blog', verbose_name='Фото')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Имя пользователя')),
            ],
        ),
    ]
