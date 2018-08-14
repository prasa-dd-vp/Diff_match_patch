from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,'app/index.html')  

def diff_match_patch(request):
    return JsonResponse({"hell0":"world"})