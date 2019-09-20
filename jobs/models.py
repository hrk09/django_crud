from django.db import models

# Create your models here.
class Job(models.Model):
    name = models.CharField(max_length=20)
    past_job = models.TextField()
# 모델 정의 하자마자 DB 작업
    # JOB의 데이터가 어떻게 정의되는 지 알려주는 함수
    def __str__(self):
        return self.name
        

