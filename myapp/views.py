from django.shortcuts import render,redirect
from myapp.models import HomeModel,BlogModel,AboutModle,ContactModel
# Create your views here.

def HomeSection(request):
    home = HomeModel.objects.all()
    blog = BlogModel.objects.all().order_by('-created_at')[:3]
    return render(request, 'index.html', {'home':home, 'blog':blog})


def BlogSection(request):
    blog = BlogModel.objects.all()
    return render(request, 'blog.html', {'blog':blog})

def BlogDetailSection(request,blog_id):
    blogdetail = BlogModel.objects.get(uuid=blog_id)
    return render(request, 'blog_detail.html', {'blogdetail':blogdetail})

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