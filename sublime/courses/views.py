from django.shortcuts import render
from .models import Articles


def courses(request):
    return render(request, 'courses/courses.html')

