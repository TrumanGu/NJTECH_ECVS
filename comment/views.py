from django.shortcuts import render,Http404
from comment.models import Subject, Teacher


def IndexView(request):
    obj = Subject.objects.all()
    return render(request, 'static/index.html', {"subject_list":obj})

def DetailView(request,sid):
    try:
        obj = Subject.objects.all().get(id=sid)
        return render(request, 'static/detail.html', {'obj':obj})
    except Exception as e:
        raise Http404('Page no found')

