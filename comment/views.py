import csv

from django.http import HttpResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.settings import api_settings
from rest_framework.viewsets import GenericViewSet
from rest_framework_csv.renderers import CSVRenderer

from .serializers import CommentSerializer
from .models import Comment
from .filters import CommentFilter


class CommentsViewSet(mixins.CreateModelMixin,
                      mixins.ListModelMixin,
                      GenericViewSet):
    serializer_class = CommentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = CommentFilter
    renderer_classes = tuple(api_settings.DEFAULT_RENDERER_CLASSES) + (CSVRenderer,)

    def get_queryset(self):
        if self.action == 'parent':
            return Comment.objects.filter(parent=None)
        if self.action == 'children':
            return Comment.objects.all()
        if self.action == 'user':
            return Comment.objects.all()
        if self.action == 'export_csv':
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

    @action(methods=["get"], detail=False)
    def export_csv(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        response = HttpResponse(content_type='text/csv')
        response.write(u'\ufeff'.encode('utf8'))
        writer = csv.writer(response)
        writer.writerow(['User', 'Date of creation', 'Parent', 'Content type', 'Related entity', 'Text'])
        for comment in queryset.values_list('user',
                                            'created_at',
                                            'parent',
                                            'content_type',
                                            'object_id',
                                            'text',
                                            ):
            writer.writerow(comment)
        response['Content-Disposition'] = 'attachment; filename="comment.csv"'

        return response
