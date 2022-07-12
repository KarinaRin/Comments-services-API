##Сервис комментариев

superuser: admin password: admin

users: user

##Доступные эндпоинты:

1. api/v1/comment/ - создание комментариев определенной сущности; вывод всех комментариев всех сущностей;
   - /?parent=False - комментарии первого уровня;
   - /?user={username} - получение истории комментариев определенного пользователя,
      доступны id пользователей: 1(admin), 2(user);
   - /?date_after={yyyy-mm-dd}&date_before={yyyy-mm-dd} - получение всех комментариев для заданного интервала времени;

2. api/v1/comment/get_children/
   - /?content_type={str}&id={int} - получение ветки комментариев по существующему id;
      доступен content_type=comment
   
3. api/v1/comment/export_csv/ - экспорт всех комментариев всех сущностей;
   - /?user={username} - получение всех комментариев для заданного пользователя,
      доступны пользователи: admin, user;
   - /?user={username}&date_after={yyyy-mm-dd}&date_before={yyyy-mm-dd} - получение всех комментариев для заданного пользователя с указание интервала времени;
   - /?content_type={str}&date_after={yyyy-mm-dd}&date_before={yyyy-mm-dd} - экспорт всей истории комментариев по заданной сущности с указание интервала времени;