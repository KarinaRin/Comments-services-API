import serpy as serpy
from rest_framework import serializers
from .models import *


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['content_type', 'object_id', 'parent', 'created_at', 'text', 'user']


# class FlatCommentUserSerializer(serpy.Serializer):
#     user = serpy.StrField(attr='user')
#
#
# class FlatCommentSerializer(serpy.Serializer):
#     id = serpy.IntField()
#     parent = serpy.StrField()
#     parent_id = serpy.IntField(required=False)
#     content_type = serpy.StrField()
#     content_type_id = serpy.IntField()
#     text = serpy.StrField()
#     object_id = serpy.IntField()
#     created_at = serpy.StrField()
#     level = serpy.IntField()
#     user = serpy.StrField()
#
#     def get_user(self, obj):
#         return FlatCommentUserSerializer(obj).data
