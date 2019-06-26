from django.shortcuts import render, redirect

from django.http import HttpResponse, JsonResponse
from django.conf import settings
import os
from .models import *
from django.core.paginator import *

def index(request):
    return HttpResponse('hello')

def detail(request, p1, p2, p3):
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

# csrf
def csrf1(request):
    return render(request, 'booktest/csrf1.html')

def csrf2(request):
    uname = request.POST['uname']
    return HttpResponse(uname)

def upload_pic(request):
    return render(request, 'booktest/upload_pic.html')

def upload_handle(request):
    pic1 = request.FILES['pic1']
    fname = os.path.join(settings.MEDIA_ROOT[0], str(pic1.name))
    with open(fname, 'wb') as f:
        for c in pic1.chunks():
            f.write(c)
    return HttpResponse(fname)


def herolist(request, pindex):
    list = HeroInfo.objects.all()
    paginator = Paginator(list, 4)
    print(pindex)
    if pindex =='':
        pindex = '1'
    page = paginator.page(int(pindex))
    context = {'page':page}
    return render(request, 'booktest/herolist.html', context)

def area(request):
    return render(request, 'booktest/area.html')

def area2(request, id):
    id1 = int(id)
    if id1 == 0:
        data = AreaInfo.objects.filter(parea__isnull=True)
    else:
        data=[{}]
    list = []
    for area in data:
        list.append([area.id, area.title])
    return JsonResponse({'data':list})

def city(request, id):
    citylist = AreaInfo.objects.filter(parea_id=id)

    list = []
    for item in citylist:
        list.append({'id':item.id, 'title':item.title})
    return JsonResponse({'data':list})

def html_editor(request):
    return render(request, 'booktest/html_editor.html')