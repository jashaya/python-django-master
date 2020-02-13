from django.shortcuts import render
from . models import Student
from . models import Registration
from . models import User
from django.http import HttpResponse
from . forms import studentForm
from . forms import signupForm
from . forms import userForm
from . forms import emailForm
from django.core.mail.message import EmailMessage
from rest_framework import generics
from . import serializers
import json
from django.core.paginator import Paginator
from .models import Post

# def display(request):
#     st=Student.objects.all()[1:5]
#     return render(request,"my_app/details.html",{'students':st})

def studentdetails(request):
    st=Student.objects.all()[1:5]
    return render(request, "my_app/studentdetails.html",  {'students':st})

def details(request,id):
    student_details=Student.objects.get(student_id=id)
    return render(request, "my_app/details.html", {'students':student_details})

def create(request):
    student1=Student(name="haya", address="tvm")
    student1.save()
    return HttpResponse("saved to db")

def createstudent(request):
    form=studentForm()
    if request.method == "POST":
        form=studentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("FORM SUBMITTED")
        else:
            return HttpResponse(form.errors)
    return render(request,"my_app/studentform.html", {'forms':form})

def signup(request):
    form=signupForm()
    if request.method=='POST':
        form=signupForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            lname=form.cleaned_data['lastname']
            address=form.cleaned_data['address']
            user = form.cleaned_data['username']
            password = form.cleaned_data['password']
            reg=Registration()
            reg.name=name
            reg.save()
            reg.lastname=lname
            reg.save()
            reg.address = address
            reg.save()
            reg.username= user
            reg.save()
            reg.password = password
            reg.save()
            return HttpResponse("FORM SUBMITTED")
        # else:
        #     return HttpResponse(form.errors)
    return render(request, "my_app/signupform.html", {'form': form})
            
def user_details(request):
    form=userForm()
    if request.method=='POST':
        form=userForm(request.POST,request.FILES)
        if form.is_valid():
            name = form.cleaned_data['username']
            image = form.cleaned_data['photo']
            user1=User()
            user1.name=name
            user1.photo=image
            user1.save()
            return HttpResponse("saved to db")
    return render(request, "my_app/userdetail.html", {'form': form})
def viewUser(request):
    userdetails=User.objects.all()
    return render(request, "my_app/userview.html", {'user': userdetails})

def getstudentdetails(request,id=2):
    st=Student.objects.get(student_id=id)
    if request.method=='POST':
        st.name=request.POST['username']
        st.address=request.POST['address']
        st.save()
        return HttpResponse("done")
    return render(request, "my_app/studentedit.html",  {'students': st})

def getname(request):
    st=Student.objects.all()
    return render(request, "my_app/studentlink.html",  {'students': st})
def getdetails(request,id):
    st_details=Student.objects.get(student_id=id)
    if request.method == 'POST':
        st_details.name = request.POST['username']
        st_details.address = request.POST['address']
        st_details.save()
        return HttpResponse("done")
    return render(request, "my_app/studentdetail.html", {'students': st_details})
def deletedetails(request,id):
    st_details = Student.objects.get(student_id=id)
    st_details.delete()
    return HttpResponse("deleted")
def emailSend(request):
    email=EmailMessage(subject="EmailDjango",
     body="first test email from django",
    from_email='techiejasna@gmail.com',
    to=['jasnamnaz@gmail.com'])
    email.send()
    return HttpResponse("Email Send Successfully")

def newmail(request):
    form = emailForm()
    if request.method == 'POST':
        form =emailForm(request.POST,request.FILES)
        if form.is_valid():
            sub = form.cleaned_data['subject']
            msg = form.cleaned_data['message']
            to = form.cleaned_data['to']
            image = form.cleaned_data['photo']
            email = EmailMessage(subject=sub,
                                 body=msg,
                                 from_email='',
                                 to=[to])
            email.attach(image.name,image.read(),image.content_type)
            email.send()
            return HttpResponse("Email Send Successfully")
    return render(request, "my_app/userdetail.html", {'form': form})
class ListStudent(generics.ListCreateAPIView):
    queryset=Student.objects.all()
    serializer_class=serializers.StudentSerializer
class DetailStudent(generics.RetrieveUpdateDestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=serializers.StudentSerializer
def search(request):
    if request.method=="POST":
        get_value=request.POST.get('username',"test")
        data={}
        data['result']="you made a request"
        return HttpResponse(json.dumps(data),content_type="application/json")
    return render(request,"my_app/userdetails.html")
def loginuser(request):
    if request.method=="POST":
        user=request.POST['username']
        request.session['user']=user
        store=request.session['user']
    return render(request,"my_app/login.html")
def sessofuser(request):
    store = request.session['user']
    # return HttpResponse("form submitted")
    return render(request,"my_app/viewsession.html",{'sess':store})

def home(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request,"my_app/page.html",{'items': posts})



