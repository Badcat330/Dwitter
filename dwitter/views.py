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
    if request.method == "POST":
        current_user_profile = request.user.profile
        data = request.POST
        action = data.get("follow")
        if action == "follow":
            current_user_profile.follows.add(profile)
        elif action == "unfollow":
            current_user_profile.follows.remove(profile)
        current_user_profile.save()
    return render(request, "dwitter/profile.html", {"profile": profile})


def dashboard(request):
    return render(request, "dwitter/dashboard.html")
