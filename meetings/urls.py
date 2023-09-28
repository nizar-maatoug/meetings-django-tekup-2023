from django.urls import path

from . import views

#domain.com/meetings/...
urlpatterns=[
    path('<int:id>',views.detail, name="detail"),    
    path('rooms', views.rooms_list, name="rooms"),
    path('new', views.new, name="new")
]