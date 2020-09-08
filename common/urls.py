from .views import IndexView, LoginView, LogoutView
from django.urls import path


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
]
