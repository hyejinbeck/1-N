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

def comment_create(request, artices_id): 
    pass 


