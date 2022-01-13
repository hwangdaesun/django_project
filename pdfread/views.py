from django.shortcuts import render
import pdfplumber
# Create your views here.
def index(request):
    context={}
    text=""
    if request.method == "POST":
        pdf = request.FILES.get("pdf")
        pdfr = pdfplumber.open(pdf)
        for i in range(len(pdfr.pages)):
            pages = pdfr.pages[i]
            text += pages.extract_text()
        pdfr.close()
        context={
            "t":text
        }
    return render(request,"pdfread/index.html", context)