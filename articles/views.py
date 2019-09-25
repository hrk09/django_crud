from django.shortcuts import render, redirect, get_object_or_404
# redirect 를 통해 article 저장 후 어떤 인덱스 페이지로 이동하세요
from .models import Article, Comment

# Create your views here.

# articles의 메인 페이지, article list를 보여줌
def index(request):
    # article 테이블에 있는 모든 게시글 가져온다
    # SELECT * FROM articles 와 같은 의미
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'articles/index.html', context)

# 입력 페이지
# GET /articles/create/
def new(request):
    return render(request, 'articles/new.html')

# 데이터를 전달 받아서 article 생성
# POST /articles/create/
def create(request):
    # 만약 POST 요청으로 들어오면 html 페이지 랜더링
    if request.method == 'POST':
        # articles/new/의 new.html의 form에서 전달받은 데이터들
        title = request.POST.get('title')
        content = request.POST.get('content')
        # article = Article()
        article = Article(title=title, content=content)
        article.save()
        # article이 생성되면, pk를 쓸 수 있으니까, 해당 pk의 상세페이지 보여주기
        # return redirect(f'/articles/{article.pk}/')
        return redirect('articles:detail', article.pk)
    # 아니라면 (GET일 경우) 사용자 데이터 받아서 article 생성
    else:
        return render(request, 'articles/create.html')

# 사용자로부터 받은 article_pk 값으로 article_pk 값에 해당하는 article 삭제
def delete(request, article_pk):
    # article = Article.objects.get(pk=article_pk)
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        article.delete()
        # return redirect('/articles/')
        return redirect('articles:index') # 첫 페이지로 갈 쑤 있게
    else:
        return redirect('articles:detail', article_pk)

# variable routing으로 사용자가 보기 원하는 페이지 pk 받아서 detail 페이지 보여주기
def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    # SELECT * FROM articles WHERE pk=3와 같은 의미
    # article = Article.objects.get(pk=article_pk)

    # 데이터 꺼내는 작업
    # comments = article.comment_set.all()
    comments = article.comments.all()

    # pk 번호 맞춰서 데이터 가져온다
    context = {
        'article': article,
        'comments': comments,
    }
    return render(request, 'articles/detail.html', context)

# update 하는 페이지 만들기
def update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    # POST로 들어오면 UPDATE 로직수행
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')

        article.title = title
        article.content = content
        article.save()
        return redirect('articles:detail', article.pk)
        # return redirect('articles:detail', article_pk) 도 가능

    # GET으로 들어오면 UPDATE하기 위한 FORM만 제공하는 페이지 제공하기
    else:
        context = {'article': article}
        return render(request, 'articles/update.html', context)
    
def comments_create(request, article_pk):
    # article_pk 에 해당하는 article에 새로운 comment 생성
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST': 
        # 생성 후, article detail page로 redirect
        content = request.POST.get('content')
        # 첫 article은 모델에 있는 article, 두번째는 pk값으로 받아온 article
        # Comment는 models class
        # comment.article = article은 어떤 article의 comment 인지 알려주기 위한 작업들(article_id나 article이나 쌤쌤)
        # comments.article_id = article_pk 랑 같음
        comments = Comment(content=content, article=article)
        comments.save()
    #     return redirect('articles:detail', article.pk)
    # else:  # GET 요청으로 들어왔을 때,
    #     return redirect('articles:detail', article.pk)

    # redirect 중복 작업 제거과정 if 되든 말든 redirect
    return redirect('articles:detail', article.pk)

def comments_delete(request, article_pk, comment_pk):
    # POST 요청으로 들어올 때 댓글 삭제 실행
    if request.method == 'POST':
        # comment_pk에 해당하는 댓글 삭제
        comment = get_object_or_404(Comment, pk=comment_pk)
        # comment가 있으면,
        comment.delete()

    # 댓글 삭제 후, detail 페이지로 이동
    return redirect('articles:detail', article_pk)