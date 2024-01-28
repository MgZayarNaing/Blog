from django.urls import path 
from myapp.views import  HomeSection,BlogSection,AboutSection,ContactSection,BlogDetailSection,loginSection,LogoutSection,SearchSection
urlpatterns = [
    path('home/', HomeSection),
    path('blog/', BlogSection),
    path('about/', AboutSection),
    path('contact/', ContactSection),
    path('blogdetail/<str:blog_id>/', BlogDetailSection),
    path('login/', loginSection, name="login"),
    path('logout/',LogoutSection, name='logout'),
    path('search/', SearchSection),
]