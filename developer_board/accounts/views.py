from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
# Create your views here.
def login(request):
    # POST 요청이 들어오면 로그인 처리를 해줌
    if request.method == 'POST':
        userid = request.POST['username']
        pwd = request.POST['password']
        #이 부분이 로그인 로그아웃의 핵심
        #장고에서는 로그인 로그아웃, 즉 데베에 저장된 회원인지 아닌지 여부를 판단해주는 내장된 기능을 알아서 제공해준다.
        #from django.contrib import auth :auth 안에 여러 메소드를 통해 특정 유저 객체가 데베있는지 아닌지를 판단해준다, 로그인/로그아웃 기능을 수행해준다.
        user = auth.authenticate(request, username=userid, password=pwd)
        #지금 사용자가 입력한 유저네임과 비번을 파이썬 변수에 저장. 이렇게 저장된 변수들이 실제로 데베에 있는 회원인지 아닌지 여부를 username과 password인자로써 확인해보겠다는 뜻
        #그리고 authenticate 메소드는 장고에 있는 이미 저장된 회원이라면 그 회원 유저 객체를 반환하고, 그렇지 않으면 None을 반환하는 메소드.
        #유저 객체? models.py에 한 번도 등록한 적이 없지만, 장고는 유저라고 하는 이미 내장된 객체를 가지고 있다.
        #createsuperuser 이 명령어를 통해 관리자 계정 생성 가능. 이 관리자 계정도 아이디와 패스워드가 있다 .우리 장고 데베 어딘가에 우리가 방금 만들어준 어드민 id, pwd가 저장되어 있다.
        #어디에 저장? 이미 내장하고 있는, 장고가 이미 갖고 있는 User 테이블 안에 있는 user 객체가 관리하고 있었던 것.
        #authenticate메소드를 통해 실제로 존재하는 id, pwd인지 존재하는 회원인지 판단하고 있다면 그 회원의 유저객체를 반환해주고, 없다면 None을 반환!
        #만약에, 유저가 실제로 존재하는 회원이라면, None이 아니라면
        if user is not None:
            auth.login(request, user)
        #auth를 통해서 로그인이라는 메소드를 통해 실제로 로그인을 할 수 있다.
            return redirect('home')
        else: #만약 유저객체가 존재하지 않는다면, None이라면
            return render(request, 'bad_login.html')
    # GET 요청이 들어오면 login form을 담고있는 login.html을 띄워주는 역할
    else:
        return render(request, 'login.html')
    
def logout(request):
    auth.logout(request)
    return redirect('home')
