from django.http import HttpRequest
from django.shortcuts import render
from .models import Student

def home(request: HttpRequest):
    if request.method == 'GET':
        msg: str = 'Welcome to Home'
        return render(request,"index.html", {'message': msg})
    
def create(request: HttpRequest):
    if request.method == 'POST':
        name = request.POST['name']
        maths = int(request.POST['maths'])
        chemistry = int(request.POST['chem'])
        physics = int(request.POST['physics'])
        # We want to insert tuple inside the model Student with the help of ORM

        response = Student.objects.create(name=name, maths=maths, chemistry=chemistry, physics=physics)
        # print(f'{response}')
        response.save()
        return render(request,'studentapp/create.html', {'success':True, 'message':'Student added successfully'})
    else:        
        return render(request,'studentapp/create.html')

def retrieve(request: HttpRequest):
    students = Student.objects.all()
    return render(request,"studentapp/retrieve.html", {'students': students})

def delete(request: HttpRequest):
    if request.method == 'POST':
        Student_id = int(request.POST['student_id'])
        student = Student.objects.get(id=Student_id)
        student.delete()
        return render(request, 'studentapp/delete.html', {'success': True, 'message': 'Student deleted successfully'})
    else:
        return render(request, 'studentapp/delete.html')
    
def update(request: HttpRequest):
    if request.method == 'POST':
        Student_id = request.POST['student_id']
        student_name = request.POST['name']
        student = Student.objects.get(id=Student_id, name=student_name)
        
        student.maths = int(request.POST['maths'])
        student.chemistry = int(request.POST['chem'])
        student.physics = int(request.POST['physics'])
        student.save()
        return render(request, 'studentapp/update.html', {'success': True, 'message': 'Student updated successfully'})
    else:
        return render(request, 'studentapp/update.html')