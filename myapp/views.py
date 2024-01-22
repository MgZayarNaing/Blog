from django.shortcuts import render
from myapp.models import HomeModel,BlogModel,AboutModle
# Create your views here.

def HomeSection(request):
    home = HomeModel.objects.all()
    blog = BlogModel.objects.all().order_by('-created_at')[:3]
    return render(request, 'index.html', {'home':home, 'blog':blog})


def BlogSection(request):
    blog = BlogModel.objects.all()
    return render(request, 'blog.html', {'blog':blog})

def AboutSection(request):
    about = AboutModle.objects.all()
    return render(request, 'contact.html', {'about':about})