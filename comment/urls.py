from django.urls import path
from .views import *

urlpatterns = [
    path('create/', CommentCreateView.as_view()),
    path('list/', CommentList.as_view()),
    path('<int:content_pk>/<int:object_pk>/', ParentCommentList.as_view()),
    path('list/<int:pk>/', CommentChildren.as_view()),
    path('list/<str:username>/', CommentUserList.as_view()),
    path('list/<int:content_pk>/<int:object_pk>/', EntityChildren.as_view()),
]
