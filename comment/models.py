from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.db import models
from mptt.models import TreeForeignKey, MPTTModel

User = get_user_model()


class Comment(MPTTModel):
    content_type = models.ForeignKey(ContentType, verbose_name='Тип сущности', on_delete=models.CASCADE,
                                     limit_choices_to={'app_label': 'comment'})
    object_id = models.PositiveIntegerField(verbose_name='ID объекта сущности')
    parent = TreeForeignKey('self', verbose_name='Родитель комментария', null=True, blank=True, db_index=True,
                            on_delete=models.CASCADE, related_name='children')
    user = models.ForeignKey(User, verbose_name='Автор комментария', on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Текст комментария')
    datetime_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        indexes = [
            models.Index(fields=['content_type', 'object_id']),
        ]

    class MPTTMeta:
        order_insertion_by = ['datetime_created']

    def __str__(self):
        return f'Comment by {self.pk}'
