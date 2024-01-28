from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib import messages
from myapp.models import HomeModel,BlogModel,AboutModle,ContactModel
from django.db.models import Q
from django.contrib.auth.models import User
# Create your views here.

def SearchSection(request):
    search = request.GET.get('search')
    home = HomeModel.objects.all()
    if search:
        blog = BlogModel.objects.filter(
            Q(title__icontains=search) |
            Q(contact__icontains=search)
            )
        return render(request, 'blog.html', {'blog':blog})
    else:
        blog = BlogModel.objects.all().order_by('-created_at')
        return render(request, 'blog.html', {'blog': blog})

def HomeSection(request):
    home = HomeModel.objects.all()
    blog = BlogModel.objects.all().order_by('-created_at')[:3]
    return render(request, 'index.html', {'home':home, 'blog':blog})


def BlogSection(request):
    blog = BlogModel.objects.all()
    return render(request, 'blog.html', {'blog':blog})

@login_required(login_url='login')
def BlogDetailSection(request,blog_id):
    blogdetail = BlogModel.objects.get(uuid=blog_id)
    blog = BlogModel.objects.all().order_by('-created_at')[:3]
    return render(request, 'blog_detail.html', {'blogdetail':blogdetail, 'blog':blog})

def AboutSection(request):
    about = AboutModle.objects.all()
    return render(request, 'about.html', {'about':about})

def ContactSection(request):
    if request.method == "GET":

        contact = ContactModel.objects.all()
        return render(request, 'contact.html', {'contact':contact})
    
    if request.method == "POST":
        contact = ContactModel.objects.create(
            firstname = request.POST.get('firstname'),
            lastname = request.POST.get('lastname'),
            email = request.POST.get('email'),
            subject = request.POST.get('subject'),
            meassage = request.POST.get('message'),
        )
        return redirect('/app/home/')

def loginSection(request):
    if request.method == "GET":
        return render(request, 'login.html')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            messages.success(request, "You are now logged in as "+ username)
            return redirect('/app/home/')
        else:
            messages.error(request, "Username or Password is incorrect!")
            return render(request, 'login.html')


def LogoutSection(request):
    logout(request)
    messages.success(request, "You are now logout! ")
    return redirect('/app/blog/')