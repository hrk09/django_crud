from django.db import models
from imagekit.processors import Thumbnail
from imagekit.models import ImageSpecField

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()  # 문자열 빈값 저장은 null이 아니라 '' 따라서 문자열 값은 null=True 넣지 말기!(이 외의 경우는 null=True)
    # 빈값(blank)이 들어와서 저장되는걸 허용함
    # blank : 데이터 유효성과 관련됨 (blank True는 즉, 그 값은 필수가 아니야)
    # null : 실제 DB 와 관련됨
    image = models.ImageField(blank=True)
    image_thumbnail = ImageSpecField(
        source='image',
        processors=[Thumbnail(200, 200)],
        format='JPEG',
        options={'quality': 90},
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# 1:N 관계 데이터 모델링 작업(1; article 이 먼저 선언되어야 N: comment 작업을 할 수 있음)
class Comment(models.Model):
    # on_delete=models.CASCADE == 'Article 이 삭제되면 Comment도 함께 삭제'
    # article.comments를 쓰고싶으면 원래는 articles.comment_set으로 쓰지만, related_name 설정하면 됨
    # relate_name == 'Article instance가 comment를 역참조할 수 있는 이름을 정의'
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    content = models.CharField(max_length=200)
    # 데이터가 추가됐을 때만, 시간 추가 auto_now_add
    crated_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # 메타데이터: 데이터를 위한 데이터 
    class Meta:
        # 데이터 순서 매기기
        ordering = ['-pk']

    def __str__(self):
        return self.content