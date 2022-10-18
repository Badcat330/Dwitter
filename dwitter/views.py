from django.shortcuts import render
from .models import Profile


def dashboard(request):
    return render(request, "base.html")


def profile_list(request):
    if request.user.is_anonymous:
        profiles = Profile.objects.all()
    else:
        profiles = Profile.objects.exclude(user=request.user)
    return render(request, "dwitter/profile_list.html", {"profiles": profiles})


def profile(request, pk):
    profile = Profile.objects.get(pk=pk)
    return render(request, "dwitter/profile.html", {"profile": profile})
