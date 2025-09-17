from django.http import HttpRequest, JsonResponse
from .models import Marksheet
from django.shortcuts import render
from django.template.loader import render_to_string
from studentapp.models import Student
from subjectapp.models import Subject

def marksheet_list(request: HttpRequest):
    try:
        marksheet = Marksheet.objects.all()
        return render(request, "marksheetapp/marksheet.html", {'marksheets' : marksheet})
    except Marksheet.DoesNotExist:
        return render (request, "marksheetapp/marksheet.html", {'massage' : 'Marksheet doesnot exsit'})
    
def add_marksheet(request: HttpRequest):
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        if not Student.objects.filter(id=student_id).exists():
            return JsonResponse({"message": "Invalid student ID"}, status=404)
        subject_id = request.POST.get("subject_id")
        if not Subject.objects.filter(id=subject_id).exists():
            return JsonResponse({"message": "Invalid subject ID"}, status=404)
        try:
            marks = int(request.POST.get("marks"))
            max_marks = int(request.POST.get("max_marks"))
            if (marks > max_marks):
                return JsonResponse({"message": "Invalid marks values"}, status=400)
        except (TypeError, ValueError):
            return JsonResponse({"message": "Marks and Max Marks must be valid integers"}, status=400)
        exam_nm = request.POST.get("exam_name")

        Marksheet.objects.create(
            student = student_id,
            subject = subject_id,
            marks = marks,
            max_marks = max_marks,
            exam_name = exam_nm,
        )
        try:
            mark_sheets = Marksheet.objects.all()
            html_markSheet = render_to_string("partial/marksheet_list.html", {"mark_sheet" : mark_sheets})
            context = {
                "mark_sheets" : html_markSheet,
                "message" : "Marksheet update successfully"
            }
            return JsonResponse(context)
        except Marksheet.DoesNotExist:
            return JsonResponse({"message": "Marksheet does not exsit"}, status=400)
        
        