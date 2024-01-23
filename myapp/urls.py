from django.urls import path 
from myapp.views import  HomeSection,BlogSection,AboutSection,ContactSection,BlogDetailSection
urlpatterns = [
    path('home/', HomeSection),
    path('blog/', BlogSection),
    path('about/', AboutSection),
    path('contact/', ContactSection),
    path('blogdetail/<str:blog_id>/', BlogDetailSection),

]