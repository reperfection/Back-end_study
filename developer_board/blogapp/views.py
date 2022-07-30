from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from django.utils import timezone
from .forms import BlogForm, BlogModelForm, CommentForm

# Create your views here.
def home(request):
    #블로그 글들을 모조리 띄우는 코드
    #posts = Blog.objects.all()
    posts = Blog.objects.filter().order_by('date')
    return render(request, 'index.html', {'posts':posts})

# 블로그 글 작성 html을 보여주는 함수
def new(request):
    return render(request, 'new.html')

#블로그 글을 저장해주는 함수
def create(request):
    if(request.method == "POST"):
        post = Blog()
        post.title = request.POST['title']
        post.body = request.POST['body']
        post.date = timezone.now()
        post.save()
    return redirect('home')

#django form을 이용해서 입력값을 받는 함수
# GET 요청과 (= 입력값을 받을 수 있는 html을 갖다 줘야됨)
# POST 요청 (= 입력한 내용을 데이터베이스에 저장. form에서 입력한 내용을 처리)
# 둘 다 처리가 가능한 함수
def formcreate(request):
            #입력 내용을 DB에 저장
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            post = Blog()
            post.title = form.cleaned_data['title']
            post.body = form.cleaned_data['body']
            post.save()
            return redirect('home')
    else:
        #입력을 받을 수 있는 html을 갖다 주면 된다
        form = BlogForm()
    return render(request, 'form_create.html', {'form':form})

def modelformcreate(request):
    #위의 그냥 폼을 복붙해도 됨
    if request.method == 'POST' or request.method == 'FILES':
        form = BlogModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BlogModelForm()
    return render(request, 'form_create.html', {'form':form})

def detail(request, blog_id):
    # blog_id 번째 블로그 글을 데이터베이스로부터 갖고와서
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    #여기서 blog_detail이란 블로그 모델 중에서 객체들 중에서 pk값이 blog_id에 해당하는 객체 하나
    #blog_id는 ursl.py에서 int:blog_id로부터 전달된 index.html에서 post.id 블로그 객체의 아이디값..보이지 않는 pk값
    # blog_id 번째 블로그 글을 detail.html로 띄워주는 코드
    
    comment_form = CommentForm()
    
    
    return render(request, 'detail.html', {'blog_detail':blog_detail, 'comment_form':comment_form})

def create_comment(request, blog_id):
    filled_form = CommentForm(request.POST)
    
    if filled_form.is_valid():
        finished_form = filled_form.save(commit=False) #filled_form을 아직은 저장하지 않고 대기. 변수에 담아준다. 
        #대기중인 변수에 post 안에 있는 models.py의 Comment 클래스의 post 변수에 Blog객체 중에서 pk값이 blog_id인 것을 담아준다.
        finished_form.post = filled_form.post = get_object_or_404(Blog, pk=blog_id)
        finished_form.save() #어떤 게시글에 달려있는 댓글인지 완벽하게 정보가 저장
        
        return redirect('detail', blog_id)