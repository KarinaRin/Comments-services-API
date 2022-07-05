
from django.http import Http404
from rest_framework import generics, viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .serializers import CommentSerializer
from .models import Comment


class CommentsViewSet(mixins.CreateModelMixin,
                      mixins.ListModelMixin,
                      GenericViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        if self.action == 'parent':
            return Comment.objects.filter(parent=None)
        return Comment.objects.all()

    @action(methods=["get"], detail=False)
    def parent(self, request, *args, **kwargs):
        return self.list(self, request, *args, **kwargs)


    # def children(self):
    #     children = self.get_queryset.get_children(include_self=True)
    #     serializer = self.get_serializer(children, many=True)
    #     return Response(serializer.data)


# class ParentCommentList(generics.ListAPIView):
#     serializer_class = CommentSerializer
#
#     def get_queryset(self):
#         return Comment.objects.filter(parent=None)




# class CommentCreateView(generics.CreateAPIView):
#     serializer_class = CommentSerializer
#
#
# class CommentList(generics.ListAPIView):
#     serializer_class = FlatCommentSerializer
#     queryset = Comment.objects.all()
#
#
# class ParentCommentList(generics.ListAPIView):
#     serializer_class = FlatCommentSerializer
#
#     def get_queryset(self):
#         return Comment.objects.filter(parent=None)\
#             .filter(content_type_id=self.kwargs['content_pk'])\
#             .filter(object_id=self.kwargs['object_pk'])
#
#
# class CommentChildren(generics.ListAPIView):
#     serializer_class = FlatCommentSerializer
#
#     def get_queryset(self):
#         try:
#             comment = Comment.objects.get(pk=self.kwargs['pk'])
#         except Comment.DoesNotExist:
#             raise Http404
#
#         return comment.get_descendants(include_self=False)
#
#
# class EntityChildren(generics.ListAPIView):
#     serializer_class = FlatCommentSerializer
#
#     def get_queryset(self):
#         return Comment.objects.filter(content_type_id=self.kwargs['content_pk'])\
#             .filter(object_id=self.kwargs['object_pk'])
#
#
# class CommentUserList(generics.ListAPIView):
#     serializer_class = FlatCommentSerializer
#
#     def get_queryset(self):
#         return Comment.objects.filter(user__username=self.kwargs['username'])
