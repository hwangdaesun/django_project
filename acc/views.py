from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import User
from django.contrib.auth.hashers import check_password
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request, "acc/index.html")

def userlogin(request):
    if request.method == "POST":
        un = request.POST.get("un")
        pw = request.POST.get("pw")
        user = authenticate(username=un, password=pw)
        if user:
            messages.success(request, "LOGIN SUCCESS")
            login(request, user)
            return redirect("acc:index")
        else:
            messages.warning(request,"가라 훠이훠이~")
            messages.error(request, "LOGIN FAIL")
    return render(request, "acc/login.html")

def userlogout(request):
    logout(request)
    return redirect("acc:index")

def signup(request):
    if request.method == "POST":
        un = request.POST.get("un")
        pw = request.POST.get("pw")
        age = request.POST.get("age")
        pic = request.FILES.get("pic")

        
        com = request.POST.get("comment")
        
        User.objects.create_user(username=un, password=pw, age=age, pic=pic, comment=com)
        messages.success(request, "회원가입이 완료되셨습니다.")
        return redirect("acc:login")
    return render(request, "acc/signup.html")

    # get안에 있는 값은 html 태그 안에 있는 속성값이다. User.objects.create_user()에서 괄호 안 각각 username같은 경우
    # 모델에서 명명한 이름 그대로를 사용하여야 한다. 그리고 각각에서 오른쪽의 경우에는 우리가 임의적으로 명명한 이름을 사용하여야한다.

def profile(request):
    return render(request, "acc/profile.html")

def user_delete(request):
    request.user.delete()
    messages.success(request, "삭제가 되었습니다.")
    return redirect("acc:index")

def update(request):
    if request.method == "POST":
        u = request.user #기존 아이디 저장
        pw = request.POST.get("pw")
        if pw:
            u.set_password(pw)

        com = request.POST.get("comment")
        if com:
            u.comment = com

        pic = request.FILES.get("pic")
        if pic:
            u.pic = pic
        
        
        u.save()
        login(request, u)
        
        return redirect("acc:profile")

    return render(request, "acc/update.html")

