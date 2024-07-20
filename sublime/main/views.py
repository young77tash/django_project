from django.shortcuts import render



def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def question(request):
    return render(request, 'main/question.html')

def money(request):
    return render(request, 'main/money.html')