from rest_framework import serializers
from .models import *


class CommentSerializer(serializers.ModelSerializer):

    def validate(self, data):

        if data['content_type'] not in ContentType.objects.all():
            raise serializers.ValidationError("This entity doesn't exist yet!")
        if not data['content_type'].model_class().objects.filter(id=data['object_id']):
            raise serializers.ValidationError("This entity's object doesn't exist yet!")
        return data

    class Meta:
        model = Comment
        fields = ['id', 'content_type', 'object_id', 'parent', 'created_at', 'text', 'user']
