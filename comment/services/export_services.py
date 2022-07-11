import csv
from django.http import HttpResponse


def export_csv(self):
    queryset = self.filter_queryset(self.get_queryset())
    response = HttpResponse(content_type='text/csv')
    response.write(u'\ufeff'.encode('utf8'))
    writer = csv.writer(response)
    writer.writerow(['User', 'Date of creation', 'Parent', 'Content type', 'Related entity', 'Text'])
    for comment in queryset.values_list('user__username',
                                        'created_at',
                                        'parent',
                                        'content_type__model',
                                        'object_id',
                                        'text',
                                        ):
        writer.writerow(comment)
    response['Content-Disposition'] = 'attachment; filename="comment.csv"'

    return response
