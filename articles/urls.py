from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'), 
    path('<int:id>/', views.detail, name='detail'),

    path('create/', views.create, name='create'),

    path('<int:article_id>/comments/create', views.comment_create, name='comment_create'),
      # articles / artices_id / comments/ create 
      # articles의 해당하는 번호(상세페이지)의 댓글을 달아주세요.

    path('<int:article_id>/comments/<int:id>/delete/', views.comment_delete, name='comment_delete'),
    # -> articles/10/comments/5/delete/
]