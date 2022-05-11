
# Create your views here.

from django.http import HttpResponse
from . models import Course


def main(request):
    return HttpResponse('<h1>main</h1>')

def show(request):
    course = Course.objects.all()
    result = ''
    for c in course:
     result += c.name + '<br>'
    return HttpResponse(result)

def insert(request):
    Course(name='데이터 분석', cnt=30).save()
    Course(name='데이터 수집', cnt=20).save()
    Course(name='웹개발', cnt=25).save()
    Course(name='인공지능', cnt=20).save()
    return HttpResponse('완료')




    