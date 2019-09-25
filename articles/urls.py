from django.urls import path
from . import views

# /articles/__
app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:article_pk>/', views.detail, name='detail'),

    # path('new/', views.new, name='new'), 둘 다 create로 들어오니까 사라져..
    path('create/', views.create, name='create'),

    # /articles/1/delete/
    path('<int:article_pk>/delete/', views.delete, name='delete'),
    path('<int:article_pk>/update/', views.update, name='update'),
    
    # /articles/3/comments/
    path('<int:article_pk>/comments/', views.comments_create, name='comments_create'),

    # /articles/3/comments/2/delete 3번 articles 댓글 중에 2번째 댓글 지우기
    path('<int:article_pk>/comments/<int:comment_pk>/delete/', views.comments_delete, name='comments_delete'),

    
]