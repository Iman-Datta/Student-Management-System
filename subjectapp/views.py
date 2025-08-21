from django.shortcuts import render
from studentapp.models import Stream
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
                subjects: QuerySet = Subject.objects.select_related("stream")
                html_string: str = render_to_string("partial/subject_rows.html",{"subjects":subjects})
                
                return JsonResponse({
                    "subjects": html_string,
                    "message": "Stream found"
                }, status=200)
            except Stream.DoesNotExist:
                return JsonResponse({"message": "Stream not found"}, status=400)

def edit_subject(request: HttpRequest):
    pass

def del_subject(request: HttpRequest):
    pass