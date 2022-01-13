from typing import KeysView
from django.shortcuts import render, redirect
from .models import Board,Reply
from django.utils import timezone
from django.core.paginator import Paginator

# Create your views here.


def index(request):
    
    pg = request.GET.get("page", 1)
    cate = request.GET.get("cate","")
    kw = request.GET.get("kw","")
    if cate == "sub":
        b = Board.objects.filter(subject__startswith=kw)
    elif cate == "wri":
        b = Board.user.username.get("kw")

    elif cate == "con":
        b = Board.objects.filter(content__contains=kw)
    else:
        b = Board.objects.all().order_by('pubdate')
    
    pag = Paginator(b,10)
    obj = pag.get_page(pg)

    context={
        "blist" : obj,
        "kw" : kw,
        "cate" : cate
       
    }
    return render(request, "board/index.html", context)

def detail(request, bpk):
    b = Board.objects.get(id=bpk)
    r = b.reply_set.all()
    context={
        "bo" : b,
        "rlist" : r
    }
    return render(request, "board/detail.html", context)

def delete(request, bpk):
    b=Board.objects.get(id=bpk)
    if b.writer == request.user:
        b.delete()
    else:
        pass # 메세지 경고창을 넣어주세요

    return redirect("board:index")

def create(request):
    if request.method == "POST":
        sub = request.POST.get("sub")
        con = request.POST.get("con")
        if sub:
            Board(subject=sub, writer=request.user, content=con, pubdate=timezone.now()).save()
        return redirect("board:index")
        

    return render(request, "board/create.html")

def update(request,bpk):
    b = Board.objects.get(id=bpk)
    
    if request.method == "POST":
        b.subject = request.POST.get("sub")
        b.content = request.POST.get("con")
        if b.writer == request.user:
            b.save()
        return redirect("board:detail", bpk=bpk)  
    context={
            "bo" : b
        }
        
    return render(request, "board/update.html", context)

def creply(request, bpk):
    b = Board.objects.get(id=bpk)    
    com = request.POST.get("com")
    Reply(b=b, replyer=request.user, comment=com, pubdate=timezone.now() ).save()

    return redirect("board:detail", bpk=bpk)

def dreply(request, bpk,rpk):
    r = Reply.objects.get(id=bpk)
    if request.user == r.replyer:
        r.delete()
    return redirect("board:detail", bpk=bpk)

def likey(request, bpk):
    b = Board.objects.get(id=bpk)
    b.likey.add(request.user)
    return redirect("board:detail", bpk=bpk)

def unlikey(request, bpk):
    b = Board.objects.get(id=bpk)
    b.likey.remove(request.user)
    return redirect("board:detail", bpk=bpk)