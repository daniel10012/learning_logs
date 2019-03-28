from django.shortcuts import render
#from django.http import HttpResponse
from logs.models import Topic, Entry
from .forms import TopicForm
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here. request is a python object rendering http request
def index(request):
    return render(request,"base.html")
    #return HttpResponse("<h1>hello django!<\h1>")

def topics(request):
    context = {}
    t = Topic.objects.all()
    context["topics"] = t
    return render(request, "topics.html",context)

def new_topic(request):
    '''add a new topic'''
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = TopicForm()
    else:
        # POST data submitted; process data
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('logs:topics'))

    return render(request, 'new_topic.html',context={"form":form})
