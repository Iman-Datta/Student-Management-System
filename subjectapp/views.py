from django.shortcuts import get_object_or_404, render
from streamapp.models import Stream
from subjectapp.models import Subject
from django.db.models.query import QuerySet
from django.http import HttpRequest, JsonResponse
from django.template.loader import render_to_string

# Create your views here.
def subject_list(request: HttpRequest):
    streams: QuerySet = Stream.objects.all()
    subjects: QuerySet = Subject.objects.select_related("stream")
    return render(request, "subjectapp/add_subject.html", {"streams" : streams, "subjects": subjects})

def add_subject(request: HttpRequest):
    if request.method == "POST":
        stream_id = request.POST.get("stream_id")       # coming from DropDown
        subject_name = request.POST.get("subject_name")
        
        # print(request.POST)
        if stream_id and subject_name:
            try:
                stream_found: Stream = Stream.objects.get(id=stream_id) # It returns an instance of the Stream model that matches
                print(f'Stream found: {stream_found}')
                
                if Subject.objects.filter(name=subject_name, stream=stream_found).exists():
                    return JsonResponse({"message": "Subject with this name exist for the selected Stream found"}, status=400)
                else:
                    Subject.objects.create(name=subject_name, stream=stream_found)
                
                # select_related('foreign_key) this function will collect all the instances of the Primary Key Model in association with the Foreign Key Model
                streams: QuerySet = Stream.objects.all()
                subjects: QuerySet = Subject.objects.select_related("stream")
                html_string: str = render_to_string("partial/subject_accordion.html",{"subjects":subjects, "streams": streams})
                
                return JsonResponse({
                    "subjects": html_string,
                    "message": "Stream added successfully"
                }, status=200)
            except Stream.DoesNotExist:
                return JsonResponse({"message": "Stream not found"}, status=400)

def edit_subject(request: HttpRequest, subject_id: int):
    if request.method == 'POST':
        subject_name = request.POST.get("subject_name")
        if not Subject.objects.filter(name = subject_name).exclude(id = subject_id).exists(): # name is a property having public access specifier in the model
            subject:Subject = Subject.objects.get(id=subject_id)
            subject.name = subject_name
            subject.save()

            streams: QuerySet = Stream.objects.all()
            subjects: QuerySet = Subject.objects.all()
            html_subject = render_to_string("partial/subject_accordion.html", {"subjects": subjects, "streams": streams})
            context = {
                "subjects": html_subject,
                "message": "Subject updated successfully"
            }
            return JsonResponse(context, status=200)
            
def del_subject(request: HttpRequest, subject_id: int):
    subject: Subject = get_object_or_404(Subject, pk=subject_id) # pk is a alias name of id which is an auto generated property of the model
    if subject is None:
        return JsonResponse({"message": "Subject not found"}, status=400)
    else:
        subject.delete()

    streams: QuerySet = Stream.objects.all()
    subjects: QuerySet = Subject.objects.select_related("stream")
    html_subject: str = render_to_string("partial/subject_accordion.html", {"subjects": subjects, "streams": streams})
    context = {
        "subjects": html_subject,
        "message": "Subject deleted successfully"
    }
    return JsonResponse(context, status=200)