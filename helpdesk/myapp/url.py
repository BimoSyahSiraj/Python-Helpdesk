from django.urls import path
from . import views

urlpatterns = [
    path('base/',views.BasePage,name="base"),
    path('login/',views.LoginView,name="login"),
]