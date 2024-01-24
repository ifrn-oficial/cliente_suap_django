from django.urls import path

from app.views import login, profile

app_name = 'app'

urlpatterns = [
    path('login/', login, name='login'),
    path('accounts/profile/', profile, name='profile')
]
