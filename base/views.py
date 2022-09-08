from curses.ascii import HT
from hashlib import new
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Announcement,Lesson,Commission,Sponsor,News
from .forms import AnnouncementForm,LessonForm,CommissionForm,SponsorForm,NewsForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.


def loginPage(request):

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        username=request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist.')

        user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'Username or password does not exist.')

    context = {}
    return render(request,'base/login.html',context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def home(request):
    announcements = Announcement.objects.all()
    lessons = Lesson.objects.all()
    commissions=Commission.objects.all()
    news=News.objects.all()
    sponsors=Sponsor.objects.all()

    context={'announcements':announcements,'lessons':lessons,'commissions':commissions,'news':news,'sponsors':sponsors}
    return render(request,'base/home.html',context)


def createAnnouncement(request):
    form = AnnouncementForm
    if request.method == "POST":
        form = AnnouncementForm(request.POST)
        if form.is_valid():
            announcement=form.save(commit=False)
            announcement.save()
            return redirect('home')
    return render(request,'base/createContent.html',{'form':form})


def createLesson(request):
    form = LessonForm

    if request.method == "POST":
        form = LessonForm(request.POST, request.FILES)
        if form.is_valid():
            lesson=form.save(commit=False)
            lesson.save()
            return redirect('home')
    return render(request,'base/createContent.html',{'form':form})


def createCommission(request):
    form = CommissionForm
    if request.method == "POST":
        form = CommissionForm(request.POST)
        if form.is_valid():
            commission=form.save(commit=False)
            commission.save()
            return redirect('home')
    return render(request,'base/createContent.html',{'form':form})


def createSponsor(request):
    form = SponsorForm
    if request.method == "POST":
        form = SponsorForm(request.POST)
        if form.is_valid():
            sponsor=form.save(commit=False)
            sponsor.save()
            return redirect('home')
    return render(request,'base/createContent.html',{'form':form})

def createNews(request):
    form = NewsForm
    if request.method == "POST":
        form = NewsForm(request.POST)
        if form.is_valid():
            news=form.save(commit=False)
            news.save()
            return redirect('home')
    return render(request,'base/createContent.html',{'form':form})


def deleteAnnouncement(request,pk):
    announcement = Announcement.objects.get(id=pk)

    if not request.user.is_superuser:
        return HttpResponse("You are not allowed here")

    if request.method == 'POST':
        announcement.delete()
        return redirect('home')

    return render(request,'base/delete.html',{'obj':announcement})


def deleteLesson(request,pk):
    lesson = Lesson.objects.get(id=pk)

    if not request.user.is_superuser:
        return HttpResponse("You are not allowed here")

    if request.method == 'POST':
        lesson.delete()
        return redirect('home')

    return render(request,'base/delete.html',{'obj':lesson})


def deleteNews(request,pk):
    new = News.objects.get(id=pk)

    if not request.user.is_superuser:
        return HttpResponse("You are not allowed here")

    if request.method == 'POST':
        new.delete()
        return redirect('home')

    return render(request,'base/delete.html',{'obj':new})


def deleteCommission(request,pk):
    comission = Commission.objects.get(id=pk)

    if not request.user.is_superuser:
        return HttpResponse("You are not allowed here")

    if request.method == 'POST':
        comission.delete()
        return redirect('home')

    return render(request,'base/delete.html',{'obj':comission})

def deleteSponsor(request,pk):
    sponsor = Sponsor.objects.get(id=pk)


    if not request.user.is_superuser:

        return HttpResponse("You are not allowed here")

    if request.method == 'POST':
        sponsor.delete()
        return redirect('home')

    return render(request,'base/delete.html',{'obj':sponsor})

def updateAnnouncement(request,pk):
    announcement = Announcement.objects.get(id=pk)
    form=AnnouncementForm(instance=announcement)

    if request.method == "POST":
            announcement.title=request.POST.get('title')
            announcement.host=request.POST.get('host')
            announcement.host_title=request.POST.get('host_title')
            announcement.body=request.POST.get('body')
            announcement.save()
            return redirect('home')
    context={'form':form}
    return render(request,'base/createContent.html',context)


def updateLesson(request,pk):
    lesson = Lesson.objects.get(id=pk)
    form=LessonForm(instance=lesson)

    if request.method == "POST":
            lesson.name=request.POST.get('name')
            lesson.tutor=request.POST.get('tutor')
            lesson.image=request.POST.get('image')
            lesson.description=request.POST.get('description')
            lesson.save()
            return redirect('home')
    context={'form':form}
    return render(request,'base/createContent.html',context)



def updateCommission(request,pk):
    commission = Commission.objects.get(id=pk)
    form=CommissionForm(instance=commission)

    if request.method == "POST":
            commission.name=request.POST.get('name')
            commission.chair=request.POST.get('chair')
            commission.description=request.POST.get('description')
            commission.save()
            return redirect('home')
    context={'form':form}
    return render(request,'base/createContent.html',context)


def updateNews(request,pk):
    new = News.objects.get(id=pk)
    form=NewsForm(instance=new)

    if request.method == "POST":
            new.title=request.POST.get('title')
            new.host=request.POST.get('host')
            new.body=request.POST.get('body')
            new.image=request.POST.get('image')
            new.save()
            return redirect('home')
    context={'form':form}
    return render(request,'base/createContent.html',context)


def updateSponsor(request,pk):
    sponsor = Sponsor.objects.get(id=pk)
    form=SponsorForm(instance=sponsor)

    if request.method == "POST":
            sponsor.name=request.POST.get('name')
            sponsor.image=request.POST.get('image')
            sponsor.save()
            return redirect('home')
    context={'form':form}
    return render(request,'base/createContent.html',context)