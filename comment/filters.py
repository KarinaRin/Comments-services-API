import django_filters
from django_filters import filters
from .models import Comment


class CommentFilter(django_filters.FilterSet):
    entity = filters.CharFilter(field_name='content_type__model')
    user = filters.CharFilter(field_name='user__username')
    date = filters.DateFromToRangeFilter(field_name='created_at')
    parent = django_filters.BooleanFilter(lookup_expr='isnull', exclude=True)

    class Meta:
        model = Comment
        fields = ['content_type',
                  'object_id',
                  'user',
                  'parent',
                  ]
