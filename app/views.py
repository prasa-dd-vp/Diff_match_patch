from django.shortcuts import render
from django.template import loader
from django.http import JsonResponse
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,'app/index.html')  

def html1(request):
    return render(request,'app/doc1.html')  

def html2(request):
    return render(request,'app/doc2.html')  

def doc1(request):
    if request.method == "POST":
        d1 = request.POST.get('d1')
        print(d1)
        return HttpResponse(d1)
    
def doc2(request):
    if request.method == "POST":
        d2 = request.POST.get('d2')
        print(d2)
        return HttpResponse(d2)    
