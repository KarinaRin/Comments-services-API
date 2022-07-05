from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.viewsets import GenericViewSet

from .serializers import CommentSerializer
from .models import Comment
from .filters import CommentFilter


class CommentsViewSet(mixins.CreateModelMixin,
                      mixins.ListModelMixin,
                      GenericViewSet):
    serializer_class = CommentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = CommentFilter

    def get_queryset(self):
        if self.action == 'parent':
            return Comment.objects.filter(parent=None)
        if self.action == 'children':
            return Comment.objects.all()
        if self.action == 'user':
            return Comment.objects.all()

        return Comment.objects.all()

    @action(methods=["get"], detail=False)
    def parent(self, request, *args, **kwargs):
        return self.list(self, request, *args, **kwargs)

    @action(methods=["get"], detail=False)
    def children(self, request, *args, **kwargs):
        return self.list(self, request, *args, **kwargs)

    @action(methods=["get"], detail=False)
    def user(self, request, *args, **kwargs):
        return self.list(self, request, *args, **kwargs)

