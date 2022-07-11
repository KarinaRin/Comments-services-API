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
from .services.export_services import export_csv


class CommentsViewSet(mixins.CreateModelMixin,
                      mixins.ListModelMixin,
                      GenericViewSet):
    serializer_class = CommentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = CommentFilter
    renderer_classes = tuple(api_settings.DEFAULT_RENDERER_CLASSES) + (CSVRenderer,)
    queryset = Comment.objects.all()

    @action(methods=["get"], detail=False)
    def export_csv(self, request):
        return export_csv(self.get_queryset())

    # def export_csv(self, request):
    #     queryset = self.filter_queryset(self.get_queryset())
    #     response = HttpResponse(content_type='text/csv')
    #     response.write(u'\ufeff'.encode('utf8'))
    #     writer = csv.writer(response)
    #     writer.writerow(['User', 'Date of creation', 'Parent', 'Content type', 'Related entity', 'Text'])
    #     for comment in queryset.values_list('user__username',
    #                                         'created_at',
    #                                         'parent',
    #                                         'content_type__model',
    #                                         'object_id',
    #                                         'text',
    #                                         ):
    #         writer.writerow(comment)
    #     response['Content-Disposition'] = 'attachment; filename="comment.csv"'
    #
    #     return response
