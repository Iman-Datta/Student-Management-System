from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Stream
from django.db.models import QuerySet

def home(request: HttpRequest):
    if request.method == 'GET':
        msg: str = 'Welcome to Home'
        return render(request,"index.html", {'message': msg})
    
def add_stream(request: HttpRequest):
    if request.method == 'POST':
        stream_name: str = request.POST['stream_name']
        if stream_name:
            if not Stream.objects.filter(name=stream_name).exists():
                Stream.objects.create(name=stream_name)
                streams: QuerySet = Stream.objects.all()
                print(streams)
                # List Comprehension
                stream_data = [ 
                    {"id": stream.id, "name": stream.name } for stream in streams
                ]
                return JsonResponse({"streams": stream_data})
            else:
                return JsonResponse({"message":"Stream already exist"}, status = 400)
        else:
            return JsonResponse({"message":"Stream name should be provided"}, status= 400)
    else:        
        return render(request,'studentapp/add_stream.html')

def retrieve(request: HttpRequest):
    students = Stream.objects.all()
    return render(request,"studentapp/retrieve.html", {'students': students})


