import json
from django.http import HttpRequest, JsonResponse
from django.template.loader import render_to_string
from django.shortcuts import render
from studentapp.models import Student
from streamapp.models import Stream


def student_list(request: HttpRequest):
    students = Student.objects.all()
    stream = Stream.objects.all()
    return render(request, 'studentapp/student.html', {'students': students, 'streams': stream})

def add_student(request: HttpRequest):
    if request.method == 'POST':
        name = request.POST.get('student_name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        dob = request.POST.get('date_of_birth')
        address = request.POST.get('address')
        guardian_name = request.POST.get('guardian_name')
        guardian_relation = request.POST.get('guardian_relation')
        guardian_contact = request.POST.get('guardian_contact')
        phoneNum = request.POST.get('phone_number')
        email = request.POST.get('email')
        stream = request.POST.get('stream')
        section = request.POST.get('section')

        if email:
            if not Student.objects.filter(email=email).exists():
                Student.objects.create(
                    name = name,
                    age = age,
                    gender = gender,
                    date_of_birth = dob,
                    address = address,
                    guardian_name = guardian_name,
                    guardian_relation = guardian_relation,
                    guardian_contact = guardian_contact,
                    phone_number = phoneNum,
                    email = email,
                    stream = stream,
                    section = section
                )
                student = Student.objects.all()
                html_student = render_to_string("partial/stream_rows.html", {"students": student})
                return JsonResponse({'students' : html_student})
            return JsonResponse({"message":"Student already exist"})