from .import views
from django.urls import path

urlpatterns=[
    path('',views.Apioverview),
    path('emplist/',views.EmpList,name="emplist"),
    path('empcreate/',views.Empcreate,name="empcreate"),
    path('empupdate/<int:pk>/',views.Empupdate,name="empupdate"),
    path('empdelete/<int:pk>/',views.Empdelete,name="empdelete"),
    
]
