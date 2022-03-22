from django.contrib import admin
from .models import *

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('userProfile', 'firstName', 'secondName','dateBirthday', 'emailProfile')
    list_display_links = ('userProfile',)
    search_fields = ('firstName', 'secondName','dateBirthday', 'emailProfile')

class CommentsAdmin(admin.ModelAdmin):
    list_display = ('user','blog','text','creation')
    list_display_links = ('user','blog','text')
    search_fields = ('text','creation')

class BlogAdmin(admin.ModelAdmin):
    list_display = ('user', 'photo', 'description', 'creation', 'photoPublish')
    list_display_links = ('user', 'photo')
    search_fields = ('creation', 'photoPublish')

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Comments, CommentsAdmin)
admin.site.register(Subcription)
admin.site.register(Blog, BlogAdmin)
# Register your models here.
