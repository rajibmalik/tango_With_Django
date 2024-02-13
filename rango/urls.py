from django.urls import path
from rango import views

app_name = 'rango'

urlpatterns = [
    path('', views.index, name='index'),
    # path function - first parameter is the string to match 
    # empty string '' a match is only found if there is nothing after
    # http://127.0.0.1:8000/ as this part is the domain name 
    # and is stripped away before django deals with it
    # the second parameter: views.index tells django what to view if 
    # there has been a match
    # the third parameter: 'index' is optional, and is a reference 
    # to what to call the view
    # this allows us to employ reverse URL matching
]