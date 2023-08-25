from django.shortcuts import render , redirect
from .models import Article, Comment   # Comment 추가 
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

    # comment목록 (1번게시글에 있는 comment만 뽑아야합니다)
    # 첫번째 방법 
    # comment_list = Comment.objects.filter(article=article)
    # 이거 안할려면, context 에 있는 comment_list 도 활중시켜야함 
    # .filter() 는 한 번 거른다.

    # 두번째 방법 (권유)
    # comment_list = article.comment_set.all()

    # 세번째 방법 (적극권장))
    # detail.html코드에서 article.comment_set.all 로 사용 

    context = {
        'article': article, 
        'comment_form': comment_form, 
        #'comment_list' : comment_list, # 추가
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
        
        # 첫번째 방법 
        # article_id를 기준으로 article obj를 가져와서 
        # 이 과정은 DB로 접근해서(SQL) 가져오는 방법이다. 
        # DB로 접근해서 가져오기때문에 다소 시간이 소요될 수 있다. 
        article = Article.objects.get(id=article_id)
        # article 컬럼에 추가한다. 
        comment.article = article 

        # 두번째 방법 
        # 사이트 속도 저하를 막기 위해 숫자 값 하나로 저장하는 방법이다.
        # comment.article_id = article_id 


        # 그리고 저장한다. 
        comment.save()

        return redirect('articles:detail', id=article_id)

def comment_delete(request, article_id, id): 
    comment = Comment.objects.get(id=id)

    comment.delete()

    return redirect('articles:detail', id=article_id)

