# coding: utf-8

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render


def index(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
    return render(request, 'index.html', {})


@login_required
def profile(request):
    return render(request, 'profile.html', {})
