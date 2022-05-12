
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from . models import Armyshop, Course


def main(request):
    return HttpResponse('<h1>main</h1>')

def show(request):
    course = Course.objects.all()
    # result = ''
    # for c in curriculum:
    # #  result += c.name + '<br>'
    # return HttpResponse(result)
    return render(
        request, 'secondapp/show.html',
        {'data':course}
    )

def insert(request):
    Course(name='데이터 분석', cnt=30).save()
    Course(name='데이터 수집', cnt=20).save()
    Course(name='웹개발', cnt=25).save()
    Course(name='인공지능', cnt=20).save()
    return HttpResponse('완료')

def army_shop(request):
    shops = Armyshop.objects.all()
    print(shops)

    return render(
        request,'secondapp/army_shop.html',
        {'data':shops}
    )


    