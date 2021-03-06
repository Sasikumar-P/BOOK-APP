from django.forms import widgets
from rest_framework import serializers
from fform.models import Post


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ( 'id','author', 'body', 'created_at', 'updated_at', 'title')

