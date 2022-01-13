from django.shortcuts import redirect, render
from .models import Book
from django.contrib import messages
# Create your views here.
def index(request):
    b = request.user.book.all()
    context={
        "blist" : b
    }
    return render(request,"book/index.html", context)

def create(request):
    if request.method == "POST":
        name = request.POST.get("s_name")
        url = request.POST.get("s_url")
        comment = request.POST.get("s_comment")
        impo = bool(request.POST.get("impo")) #impo가 none으로 들어간다.. 미리 print로 확인해보는 습관 들이도록!
        Book(user=request.user, site_name=name, site_url=url, comment=comment, impo=impo).save()
        return redirect("book:index")
    return render(request, "book/create.html")

def delete(request, dpk):
    a = Book.objects.get(id=dpk)
    if request.user == a.user:
        a.delete()
    else:
        messages.warning(request, "풋?")
    return redirect("book:index")