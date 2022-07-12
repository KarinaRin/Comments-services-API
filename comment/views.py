from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import serializers
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

    def get_queryset(self):
        content_type = self.request.query_params.get('content_type')
        id_params = self.request.query_params.get('id')
        filtered_qs = self.filter_queryset(super().get_queryset())
        if self.action != 'export_csv':
            if content_type or id_params:
                if not content_type or not id_params:
                    raise serializers.ValidationError("Invalid parameter, content_type and id_params should have value")
        if self.action == 'get_children':
            return filtered_qs.get_descendants(include_self=True)
        return Comment.objects.all()

    @action(detail=False, methods=['get'])
    def get_children(self, request):
        return Response(self.get_serializer(self.get_queryset(), many=True).data)

    @action(methods=["get"], detail=False)
    def export_csv(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        return export_csv(queryset)

