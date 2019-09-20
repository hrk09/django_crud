from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# 1:N 관계 데이터 모델링 작업(1; article 이 먼저 선언되어야 N: comment 작업을 할 수 있음)
class Comment(models.Model):
    # on_delete=models.CASCADE == 'Article 이 삭제되면 Comment도 함께 삭제'
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
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