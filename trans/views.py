from django.shortcuts import render
from googletrans import Translator
# Create your views here.
def index(request):
   context={}
   if request.method == "POST":
      translator = Translator()
      f = request.POST.get("from") #번역전 언어선택
      t = request.POST.get("to") #번역할 언어선택
      bef = request.POST.get("bef") #번역할 내용
      trans = translator.translate(bef, src=f, dest=t)
      context = {
         "trans" : trans.text
      }
   return render(request, "trans/index.html", context)