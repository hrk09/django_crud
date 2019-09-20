from django.urls import path
from . import views

app_name = 'jobs'

urlpatterns = [
    path('past_job/', views.past_job, name='past_job'),
    # path('name/', views.name, name='name'),    
    path('', views.name, name='name'),
]