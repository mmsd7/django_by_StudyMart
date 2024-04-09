from django.shortcuts import render

def machine_learning(request):
    return render(request,'Machine_Learning/machine_learning.html')


def random_forest(request):
    return render(request,'Machine_Learning/rf.html')

def data_tree(request):
    return render(request,'Machine_Learning/dt.html')

def kn(request):
    return render(request,'Machine_Learning/kn.html')

