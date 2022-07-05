from rest_framework import serializers
from .models import *


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['id', 'content_type', 'object_id', 'parent', 'created_at', 'text', 'user']
