from django.shortcuts import render, redirect
# redirect 를 통해 article 저장 후 어떤 인덱스 페이지로 이동하세요
from .models import Article

# Create your views here.

# articles의 메인 페이지, article list를 보여줌
def index(request):
    # article 테이블에 있는 모든 게시글 가져온다
    # SELECT * FROM articles 와 같은 의미
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'articles/index.html', context)

# 입력 페이지
def new(request):
    return render(request, 'articles/new.html')

# 데이터를 전달 받아서 article 생성
def create(request):
    # articles/new/의 new.html의 form에서 전달받은 데이터들
    title = request.GET.get('title')
    content = request.GET.get('content')

    article = Article()
    article = Article(title=title, content=content)
    article.save()
    # article이 생성되면, pk를 쓸 수 있으니까, 해당 pk의 상세페이지 보여주기
    # return redirect(f'/articles/{article.pk}/')
    return redirect('articles:detail', article.pk)

# 사용자로부터 받은 article_pk 값으로 article_pk 값에 해당하는 article 삭제
def delete(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    article.delete()
    # return redirect('/articles/')
    return redirect('articles:index') # 첫 페이지로 갈 쑤 있게

# variable routing으로 사용자가 보기 원하는 페이지 pk 받아서 detail 페이지 보여주기
def detail(request, article_pk):
    # SELECT * FROM articles WHERE pk=3와 같은 의미
    article = Article.objects.get(pk=article_pk)
    # pk 번호 맞춰서 데이터 가져온다
    context = {'article': article}
    return render(request, 'articles/detail.html', context)
