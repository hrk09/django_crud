# Media 파일 올리기 위한 작업

1. `Article Model`에 `ImageField` 추가

   - 실제 DB에 반영

     ```python
     python manage.py makemigrations
     python manage.py migrate
     ```

2. `Form`에서 파일 타입을 보낼 수 있도록 `enctype` 속성을 `multipart/form-data`로 줌

3. `Form` 안에서 `input` 생성. `accept="image/*"` 속성을 줌

   - `accept` : 특정 파일 타입만 받을 수 있게 하기 위한 속성

4. `create`함수에서 파일을 `request.FILES`에서 꺼냄

5. `media` 파일들을 저장하기 위한 폴더 설정

   ```python
   # settings.py
   MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # 프로젝트/media/
   ```

6. `media` 파일들로 접근할 수 있는 `URL` 이름 설정

   ```PYTHON
   # settings.py
   MEDIA_URL = '/media/'
   ```

7. `Client` 가 실제 파일들로 접근할 수 있는 `URL` 생성

   ```PYTHON
   # crud/urls.py
   from django.conf import settings
   from django.conf.urls.static import static
   
   ...
   
   # MEDIA_URL로 들어오면 MEDIA_ROOT에 저장한 파일들로 접근할 수 있다.
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
   ```

8. `Detail` 페이지에서 이미지 보여주기

   `detail.html`

   ```django
   <img src="{{ article.image.url }}" alt="{{ article.image }}">
   ```

   

