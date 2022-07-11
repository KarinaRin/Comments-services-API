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

