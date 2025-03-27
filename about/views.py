from django.shortcuts import render, get_object_or_404
from .models import About

def about_detail(request):
    about = About.objects.first()

    return render(
        request,
        "about/about.html",
        {"about": about},
    )