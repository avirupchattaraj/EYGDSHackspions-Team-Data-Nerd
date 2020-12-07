from django.urls import include,path
from . import views

urlpatterns = [
    path("",views.twitterhome,name='twitterhome'),
    path("options/",views.options,name='options'),
    path("inputform1/",views.inputform1,name="inputform1"),
    path("inputform2/",views.inputform2,name="inputform2"),
    path("inputform3/",views.inputform3,name="inputform3"),
    path("inputform4/",views.inputform4,name="inputform4"),
    path("result/",views.result,name='result')    
]