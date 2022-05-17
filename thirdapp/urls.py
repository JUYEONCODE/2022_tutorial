from django.urls import path
from . import views
import thirdapp

app_name = 'thirdapp'

urlpatterns = [
    path('shop/', views.shop),
    path('jeju_olle/', views.jeju_olle, name='jeju_olle'),
    path('jeju_olle/ajax/', views.jeju_olle_ajax),
    path('owner/', views.owner),
    path('hospital/', views.hospital),
    path('owner/save/', views.owner_save),

]