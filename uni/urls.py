from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(template_name='uni/index.html'), name="index"),
]
