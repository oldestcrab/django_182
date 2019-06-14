from django.shortcuts import render, redirect

from django.http import HttpResponse

def index(reqeust):
    return HttpResponse('hello')

def detail(reqeust, p1, p2, p3):
    return HttpResponse('year:{p1},month:{p2},day:{p3}'.format(p1=p1, p2=p2, p3=p3))

def get_test1(request):
    return render(request, 'booktest/get_test1.html')

def get_test2(request):
    a1 = request.GET['a']
    b1 = request.GET['b']
    c1 = request.GET['c']
    context = {'a':a1, 'b':b1, 'c':c1}
    return render(request, 'booktest/get_test2.html', context)

def get_test3(request):
    a1 = request.GET.getlist('a')
    context = {'a':a1}
    return render(request, 'booktest/get_test3.html', context)

def post_test1(request):

    return render(request, 'booktest/post_test1.html')

def post_test2(request):
    uname = request.POST['uname']
    upwd = request.POST['upwd']
    ugender = request.POST['ugender']
    uhobby = request.POST.getlist('uhobby')
    context = {'uname':uname, 'upwd':upwd, 'ugender':ugender, 'uhobby':uhobby}
    return render(request, 'booktest/post_test2.html', context)

def session1(request):
    uname = request.session.get('myname')
    context = {'uname':uname}

    return render(request, 'booktest/session1.html', context)

def session2(request):


    return render(request, 'booktest/session2.html')

def session2_handle(request):

    uname = request.POST['uname']
    request.session['myname'] = uname
    return redirect('/booktest/session1/')

def session3(request):
    del request.session['myname']
    return redirect('/booktest/session1/')