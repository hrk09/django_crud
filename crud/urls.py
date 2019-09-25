"""crud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# settins.py 불러오는 작업
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('jobs/', include('jobs.urls')),
    # articles로 들어왔다면 articles/urls.py로 이동하라는 명령
    path('articles/', include('articles.urls')),
    path('admin/', admin.site.urls),
    # media라는 url로 접근하면 저기에 저장하세요
    # static('/media/', 'BASE_DIR/media'),
]

# 사용자가 Media 파일이 있는 곳으로 올 수 있는 경로 추가(url 추가하면 사용자가 media로 갈 수 있게 됨)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)