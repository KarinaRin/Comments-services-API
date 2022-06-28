from django.http import Http404
from rest_framework import generics
from .serializers import *
from .models import Comment


class CommentCreateView(generics.CreateAPIView):
    serializer_class = CommentSerializer


class CommentList(generics.ListAPIView):
    serializer_class = FlatCommentSerializer
    queryset = Comment.objects.all()


class ParentCommentList(generics.ListAPIView):
    serializer_class = FlatCommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(parent=None)\
            .filter(content_type_id=self.kwargs['content_pk'])\
            .filter(object_id=self.kwargs['object_pk'])


class CommentChildren(generics.ListAPIView):
    serializer_class = FlatCommentSerializer

    def get_queryset(self):
        try:
            comment = Comment.objects.get(pk=self.kwargs['pk'])
        except Comment.DoesNotExist:
            raise Http404

        return comment.get_descendants(include_self=False)


class EntityChildren(generics.ListAPIView):
    serializer_class = FlatCommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(content_type_id=self.kwargs['content_pk'])\
            .filter(object_id=self.kwargs['object_pk'])


class CommentUserList(generics.ListAPIView):
    serializer_class = FlatCommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(user__username=self.kwargs['username'])
