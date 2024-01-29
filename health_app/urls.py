from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import index, prediction,home

urlpatterns = [
    path('', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('health_app-index/', index, name='health_app-index'),
    path('prediction/', prediction, name='health_app-prediction'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
