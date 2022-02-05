from django.urls import path
from django.contrib.auth.views import LogoutView as Logout

from .views import LoginPage, AccountPage, Register

urlpatterns = [
    path('login/', LoginPage.as_view(), name='login'),
    path('account/', AccountPage.as_view(), name='account'),
    path('logout/', Logout.as_view(next_page='landing_page'), name='logout'),
    path('register/', Register.as_view(), name='register'),
]
