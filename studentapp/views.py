from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse("Hello, Student App is working!")

def student_list(request: HttpRequest):
    pass
