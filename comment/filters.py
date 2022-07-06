import django_filters
from django.db.models import Q
from rest_framework import request

from .models import Comment


class CommentFilter(django_filters.FilterSet):

    # interval = django_filters.CharFilter(field_name='interval', method='interval_filter')
    # content_type__ge = django_filters.NumberFilter(field_name='content_type__id', lookup_expr='created_at__ge')
    # content_type__le = django_filters.NumberFilter(field_name='content_type__id', lookup_expr='created_at__le')
    # user__ge = django_filters.NumberFilter(field_name='user__id', lookup_expr='created_at__ge')
    # user__le = django_filters.NumberFilter(field_name='user__id', lookup_expr='created_at__le')
    created_at__gte = django_filters.DateFilter(field_name='created_at', lookup_expr='gte')
    created_at__lte = django_filters.DateFilter(field_name='created_at', lookup_expr='lte')

    class Meta:
        model = Comment
        fields = ['content_type',
                  'object_id',
                  'user',
                  'created_at'
        ]

    # def interval_filter(self, queryset):
    #     before = request.query_params.get('fromDate', None)
    #     after = request.query_params.get('toDate', None)
    #     return queryset.filter(Q(created_at__gte=before), Q(pick_up__lte=after))


