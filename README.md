##Сервис комментариев

superuser: admin password: admin

users: author1, subscriber

##Доступные эндпоинты:

1. api/v1/comment/create/ - создание комментариев определенной сущности;
2. api/v1/comment/list/ - вывод всех комментариев всех сущностей;
3. api/v1/comment/content_pk/object_pk/ - вывод комментариев первого уровня определенного объекта сущности;
   * content_pk - ID сущности 
   * object_ok - ID объекта сущности

4. api/v1/comment/list/pk/ - вывод дочерних комментариев для заданного комментария;
5. api/v1/comment/list/username/ - вывод истории комментариев для заданного пользователя; 
6. api/v1/comment/list/content_pk/object_pk/ - вывод дочерних комментариев определенного объекта сущности;

