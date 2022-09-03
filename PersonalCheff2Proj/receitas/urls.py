from platform import python_branch


from django.urls import path
from. import views

urlpatterns = [
    path('', views.index, name='index')
]