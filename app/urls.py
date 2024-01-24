from django.urls import path

from app.views import login, logout, profile

app_name = 'app'

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('accounts/profile/', profile, name='profile')
]
