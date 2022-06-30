from django.urls import path, include
from .router import router

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/', include(router.urls))
]