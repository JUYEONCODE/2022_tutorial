
# Create your views here.

from django.http import HttpResponse


def main(request):
    return HttpResponse('<h1>main</h1>')