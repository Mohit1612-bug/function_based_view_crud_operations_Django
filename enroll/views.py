from django.shortcuts import render,HttpResponseRedirect
from .forms import StudentRegistration
from .models import User
# Create your views here.
def home(request):
    if request.method=="POST":
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
            name=request.POST['name']
            email=request.POST['email']
            password=request.POST['password']
            reg=User(name=name,email=email,password=password)
            reg.save()
    else:
        fm=StudentRegistration()
    stud=User.objects.all()
    return render(request=request,template_name="enroll/addandview.html",context={'form':fm,'student':stud})


def delete_data(request,id):
    if request.method=="POST":
        pi=User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')

def update(request,id):
    if request.method=="POST":
        pi=User.objects.get(pk=id)
        fm=StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi=User.objects.get(pk=id)
        fm=StudentRegistration(instance=pi)
    return render(request=request,template_name="enroll/update.html",context={'form':fm})
