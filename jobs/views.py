from django.shortcuts import render
from .models import Job
from faker import Faker

def name(request):
    return render(request, 'jobs/name.html')


def past_job(request):
    if request.method == 'POST':
        fake = Faker('ko_kr')
        # POST에서 name 을 가져오는 작업
        name = request.POST.get('name')
        profile_image = request.FILES.get('profile_image')

        # DB에 name으로 저장된 전생직업 있는 지 확인하고, 있다면 그냥 보여줌
        if Job.objects.filter(name=name):
            job = Job.objects.get(name=name)
            job.profile_image = profile_image
            job.save()

        # 없다면, 새로 만들어서 저장 후 보여줌
        else:
            job = Job(name=name)
            job.past_job = fake.job()
            job.profile_image = profile_image
            job.save()
        context = {'job':job}
        return render(request, 'jobs/past_job.html', context)

    # 두 번째 방법
    # job = if Job.objects.filter(name=name).first()
    # if job:
    #     context = {'person':job}
    # else:
    #     fake = Faker('ko-KR')
    #     job = Job(name=name, profile_image=profile_image)
    #     job.past_job = fake.job()
    #     job.save()
    #     context = {'job': job}
    # return render(request, 'jobs/past_life.html', context)