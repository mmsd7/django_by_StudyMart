from django.shortcuts import render

def about(request):
    return render(request,'About/about.html')
