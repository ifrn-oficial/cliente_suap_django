from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from app.models import Usuario


def login(request):
    if request.user.is_authenticated:
        return redirect(reverse('app:profile'))
    return render(
        request,
        'app/pages/login.html',
        {
            'title': 'Login'
        }
    )


@login_required(login_url='/login/')
def profile(request):
    usuario = get_object_or_404(Usuario, matricula=request.user.username)
    return render(
        request, 
        'app/pages/profile.html',
        {
            'titulo': f'Perfil - {usuario.nome_completo}',
            'usuario': usuario
        }
    )


@login_required(login_url='/login/')
def logout(request):
    auth_logout(request)
    return redirect(reverse('app:login'))
