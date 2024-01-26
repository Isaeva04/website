from django.shortcuts import render


def about(request):
    return render(request,'about.html')

def contacts(request):
    return render(request,'contacts.html')

def home(request):
    return render(request,'home.html')

def blog(request):
    return render(request,'blog.html')

def questions(request):
    return render(request,'questions.html')
