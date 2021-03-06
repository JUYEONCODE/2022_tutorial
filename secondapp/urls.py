from django.urls import path
from secondapp import views

app_name = 'secondapp'

urlpatterns = [
    path('main/', views.main),
    path('insert/', views.insert),
    path('show/', views.show, name = 'show'),
    path('army_shop/', views.army_shop, name = 'army_shop'),
    path('army_shop/<int:year>/<int:month>/', views.army_shop2),
    path('req/ajax/', views.req_ajax_exam),
    path('course/save/', views.course_save),
]
