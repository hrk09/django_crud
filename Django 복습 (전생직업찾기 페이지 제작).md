# Django 복습 (전생직업찾기 페이지 작성)



### # 활용 개념

- `URL` 연결하기 (**해당 `APP`에 `urls.py` 파일 생성하는 것)

- `SQLITE3` 이용한 `DB` 작업

- `POST method` 사용한 입력 페이지, 결과페이지 `html` 파일 구성(`form` 작성)
  
  - `CRUD > templates > base.html` 활용
  
- `faker` 라이브러리 사용한 랜덤데이터 생성

  

---



### # 문제해결과정



#### 1.  jobs 폴더 생성 



##### 1) jobs를 APP으로 사용하기 위해 `CRUD > INSTALLED_APPS`에 출생신고

##### 2) `/jobs/` 을 입력하면, `CRUD > urls.py` 에서 `jobs/urls.py`로 이동하라는 명령

  ```python
  from django.urls import path, include
  
  urlpatterns = [
      path('jobs/', include('jobs.urls')),
      path('articles/', include('articles.urls')),
      path('admin/', admin.site.urls),
  ]
  
  ```

##### 3)  jobs 폴더 내 url 작업을 하기 위해 `urls.py` 폴더 생성

  ```python
  from django.urls import path
  # 현재폴더(.)
  from . import views
  
  # app_name 설정
  app_name = 'jobs'
  
  urlpatterns = [
      path('past_job/', views.past_job, name='past_job'),
      # 기본 페이지('')를 name이라는 이름으로 지정한다    
      path('', views.name, name='name'),
  ]
  
  ```

---



#### 2. DB 작업하기(SQLITE3, models.py)



##### 1) DB 작업 위해 `jobs > models.py`에서 `Job model` 생성

- `name, past_job cloumn` 정의

```python
from django.db import models

class Job(models.Model):
    name = models.CharField(max_length=20)
    # 직업은 길 수도 있으니까 TextField
    past_job = models.TextField()
    
    # Job의 데이터가 어떤 식으로 표현되는지 정의하는 함수
    def __str__(self):
    return self.name

```

- *모델 정의 하자마자 DB 작업을 하는 게 좋다(까먹을 수 있으니까..)* 

  

##### 2) `$ python manage.py makemigrations` 로 DB 작성 할 것이라는 선언문 확인

##### 3) `$ python manage.py migrate` 로 `DB TABLE` 작성

- 서버 켜서 데이터 넣어보면서 잘 들어가는 지 확인하기
- *[주의] 이 때 DB에 이미 데이터가 저장된 경우, 오류가 발생할 수 있으므로 반드시 DB 내 데이터가 없는 것을 확인해야함**( `ctrl + shift + p` 로 `sqlite3`  DB  TABLE 확인 가능 )*

------



#### 3. views.py에서 name, past_job 함수 정의하기

```python
from django.shortcuts import render
from .models import Job
# 랜덤으로 값을 보여주는 라이브러리
from faker import Faker

# 1. name 함수
# name 페이지는 그냥 입력만 하는 페이지니까, 손 댈 게 없다
def name(request):
    return render(request, 'jobs/name.html')

# 2. past_job 함수
# past_job 페이지는 name 페이지에서 입력한 name 데이터를 가져와햐 하니까 추가 작업 필요
def past_job(request):
    # faker 사용하기 위한 설정
    fake = Faker('ko_kr')
    
    # name 페이지에서 POST 했던 name 을 가져오는 작업
    name = request.POST.get('name')

    # DB에 name으로 저장된 전생직업 있는 지 확인하고, 있다면 그냥 보여줌(filter 개념)
    if Job.objects.filter(name=name):
        job = Job.objects.get(name=name)
        
    # 없다면, fake를 사용해 랜덤 직업을 매칭해 저장하고 보여줌
    else:
        job = Job(name=name)
        job.past_job = fake.job()
        job.save()
    context = {'job':job}
    return render(request, 'jobs/past_job.html', context)

```

---



#### 4. html 페이지 구성(입력 페이지, 결과 페이지)



##### 1) 베이스 작업

​	`templates`폴더 만들고, `templates` 폴더 내 `html` 작업을 할 `jobs` 폴더 생성



##### 2) 입력페이지 (name.html)

- `extends 'base.html'`하면, `crud>templates>base.html` 사용 가능
- `form` 작성 시, 해당 `form`을 `jobs`에 있는 `past_job url`로 보낸다는 설정이 필요함
  - 이 때, 해당 `form`에 작성된 데이터가 `POST method`로 제출되어야 입력한 데이터가 주소창에 노출되지 않는다. (GET은 데이터 노출)
  - `POST method` 로 데이터가 제출되어야 사용자가 우리가 제공하는 인터페이스로만(`html` 에서 만든 `form tag`) 요청을 보낼 수 있음
  - *[주의] `POST`는 반드시 `{% csrf_token %}`을 해야 함!!!!!!*

```django
{% extends 'base.html' %}

{% block title %}이름 입력 페이지{% endblock title %}

{% block body %}
<h1>전생 직업 찾기</h1>

{% comment %} 하단의 jobs는 app_name 가리킴  {% endcomment %}
<form action="{% url 'jobs:past_job' %}" method="POST">
  {% csrf_token %}
  <input type="text" placeholder="이름을 입력해주세요." name="name">
  <button type="submit">[찾아보기]</button>
    
</form>
{% endblock body %}

```



##### 3) 결과페이지 (past_job.html)

```django
{% extends 'base.html' %}

{% block title %}전생 결과 보여주는 페이지{% endblock title %}

{% block body %}
  <h1>{{ job.name }}님의 전생 직업 결과: <span style="color: blue">{{ job.past_job }}</span></h1>

  <a href=" {% url 'jobs:name' %} ">[뒤로가기]</a>
{% endblock body %}

```

