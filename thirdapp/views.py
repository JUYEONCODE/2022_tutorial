from urllib import request
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Hospital, Shop,JejuOlle, Owner

from django.shortcuts import redirect
from .forms import OwnerForm

def owner_save(request):
    if request.method == 'POST':
        form = OwnerForm(request.POST)
        if form.is_valid():
        
            c = form.save(commit=False)
            c.save()

            return redirect('/third/owner/save/')
    else:
        form = OwnerForm()

    return render(
        request, 'thirdapp/owner_save.html',
        { 'form': form }
)




def shop(request):
    shop_list = Shop.objects.all()
    
    return render(
        request,
        'thirdapp/shop.html',
        {'shop_list': shop_list}
)




def jeju_olle(request):
    # jeju_olle_list = JejuOlle.objects.all()
    time = request.GET.get('time')
    if not time: time = ''
    jeju_olle_list = JejuOlle.objects.filter(
        time_info__contains=time)
    
    return render(
        request,
        'thirdapp/jeju_olle.html',
        {'jeju_olle_list': jeju_olle_list}
)

def jeju_olle_ajax(request):
    return render(
        request, 'thirdapp/jeju_olle_ajax.html', {})




def owner(request):
  if request.method == 'POST':
    name = request.POST.get('name')

    owner = Owner(name=name)
    owner.save()

    return HttpResponse('주인 정보 등록 완료')
  return render(request, 'thirdapp/owner.html', {})


def hospital(request): 
    hospitals = Hospital.objects.all()

    return render(request, 
    'thirdapp/hospital.html', 
    {'hospitals': hospitals}
    )