from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def blog(request):
    return render(request,'Blog/blog.html')
