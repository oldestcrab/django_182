from django.shortcuts import render

from django.http import HttpResponse

def index(reqeust):
    return HttpResponse('hello')

def detail(reqeust, p1, p2, p3):
    return HttpResponse('year:{p1},month:{p2},day:{p3}'.format(p1=p1, p2=p2, p3=p3))

def get_test1(request):
    return render(request, 'booktest/get_test1.html')

def get_test2(request):
    return render(request, 'booktest/get_test2.html')

def get_test3(request):
    return render(request, 'booktest/get_test3.html')