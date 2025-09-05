from django.http import HttpRequest, JsonResponse
from .models import Marksheet
from django.shortcuts import render

def marksheet_list(request: HttpRequest):
    try:
        marksheet = Marksheet.objects.all()
        return render(request, "marksheetapp/marksheet.html", {'marksheets' : marksheet})
    except Marksheet.DoesNotExist:
        return render (request, "marksheetapp/marksheet.html", {'massage' : 'Marksheet doesnot exsit'})