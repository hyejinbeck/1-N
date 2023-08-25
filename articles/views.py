from django.shortcuts import render , redirect
from .models import Article
from .forms import ArticleForm, CommentForm # , CommentForm 추가 

# Create your views here.
def index(request): 
    articles = Article.objects.all()

    context = {
        'articles' : articles , 
    }

    return render(request, 'index.html', context)

def create(request): 
    if request.method == 'POST': # post요청일때 
        form = ArticleForm(request.POST)   # 프론트엔드에 검증
        if form.is_valid():           #통과되면 백엔드에 재검증
            form.save()            # 다 통과된것만 저장 

            return redirect('articles:index') # 일단 index로 보내보자.

    else:                     # get요청일때  
        form = ArticleForm()

    context = {
        'form': form,
    }

    return render(request, 'form.html', context)


def detail(request,id):
    article = Article.objects.get(id=id)
    comment_form = CommentForm()    # 추가 

    context = {
        'article': article, 
        'comment_form': comment_form, # 추가 
    }
    
    return render(request, 'detail.html', context)

def comment_create(request, article_id): 

    # 사용자가 입력한 정보를 form에 입력
    comment_form = CommentForm(request.POST)  

    # 유효성 검사 (프론트엔드)
    if comment_form.is_valid():  
        # form을 저장(백엔드)-> 추가로 넣어야 하는 데이터를 넣기 위해, 저장 멈춰!
        comment = comment_form.save(commit=False)
        # 어떤 데이터가 필요하다? 그럼 잠깐 저장 멈춰 
        
        # article_id를 기준으로 article obj를 가져와서 
        article = Article.objects.get(id=article_id)

        # article 컬럼에 추가한다. 
        comment.article = article 

        # 그리고 저장한다. 
        comment.save()

        return redirect('articles:detail', id=article_id)


