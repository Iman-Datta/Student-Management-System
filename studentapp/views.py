import json
from django.http import HttpRequest, JsonResponse
from django.template.loader import render_to_string
from django.shortcuts import get_object_or_404, render
from studentapp.models import Student
from streamapp.models import Stream


def student_list(request: HttpRequest):
    if request.method == 'GET':
        students = Student.objects.all()
        stream = Stream.objects.all()
        return render(request, 'studentapp/student.html', {'students': students, 'streams': stream})

def add_student(request: HttpRequest):
    if request.method == 'POST':
        name = request.POST.get('student_name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        # dob = request.POST.get('dob')
        address = request.POST.get('address')
        guardian_name = request.POST.get('guardian_name')
        guardian_relation = request.POST.get('guardian_relation')
        guardian_contact = request.POST.get('guardian_contact')
        phoneNum = request.POST.get('phone_number')
        email = request.POST.get('email')
        stream_id = request.POST.get('stream')
        section = request.POST.get('section')
        profile_pic = request.FILES.get('profile_pic')
        # print(request.FILES)
        # print(" ")
        # print(profile_pic)
        
        if email:
            if not Student.objects.filter(email=email).exists():
                try:
                    stream_obj = Stream.objects.get(id=stream_id)
                except Stream.DoesNotExist:
                    return JsonResponse({"message": "Invalid Stream selected"}, status=400)
                Student.objects.create(
                    name = name,
                    age = age,
                    gender = gender,
                    # date_of_birth = dob,
                    address = address,
                    guardian_name = guardian_name,
                    guardian_relation = guardian_relation,
                    guardian_contact = guardian_contact,
                    phone_number = phoneNum,
                    email = email,
                    stream = stream_obj,
                    section = section,
                    profile_picture=profile_pic,
                )
                try:
                    student = Student.objects.all()
                    html_students = render_to_string("partial/student_rows.html", {"students": student})
                    context = {
                        'students' : html_students,
                        'message' : "Student Added Successfully"
                    }
                    return JsonResponse(context)
                except Student.DoesNotExist:
                    return JsonResponse({"message": "Student not found"}, status = 400)
            return JsonResponse({"message":"Student already exist"}, status = 400)

def student_profile(request: HttpRequest, student_id: int):
    try:
        student = Student.objects.get(id = student_id)
        html_student = render_to_string("partial/student_profile.html", {"student": student})
        return JsonResponse({'student' : html_student}, status = 200)
    except Student.DoesNotExist:
        return JsonResponse({"message": "Student not found"}, status=404)
    except Exception as e:
        return JsonResponse({"message": str(e)}, status=500)
    
def edit_student(request: HttpRequest, student_id: int):
    try:
        student: Student = Student.objects.get(id = student_id)
        if request.method == 'POST':
            student.address = request.POST.get("address")
            student.guardian_name = request.POST.get("guardian_name")
            student.guardian_relation = request.POST.get("guardian_relation")
            student.guardian_contact = request.POST.get("guardian_contact")
            student.phone_number = request.POST.get("phone_number")
            student.email = request.POST.get("email")
            student.profile_picture = request.FILES.get('profile_pic')
            student.save()

            try:
                students = Student.objects.all()
                html_students = render_to_string("partial/student_rows.html", {"students": students})
                context = {
                        'students' : html_students,
                        'message' : "Student Updated Successfully"
                    }
                return JsonResponse(context)
            except Student.DoesNotExist:
                return JsonResponse({"message": "Student not found"}, status = 400)
    except Student.DoesNotExist:
        return JsonResponse({"message": "Student not found"}, status = 400)
    
def del_student(request: HttpRequest, student_id: int):
    try:
        student = Student.objects.get(id = student_id)
        student.delete()
        try:
            students = Student.objects.all()
            html_students = render_to_string("partial/student_rows.html", {"students" : students})
            return JsonResponse({'students' : html_students})
        except Student.DoesNotExist:
            return JsonResponse({"message" : "No student found"})
        except Exception as e:
            return JsonResponse({"message" : str(e)}, status = 500)
    except Student.DoesNotExist:
        return JsonResponse({"message" : "No student found"})
    except Exception as e:
        return JsonResponse({"message" : str(e)}, status = 500)