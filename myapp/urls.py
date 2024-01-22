from django.urls import path 
from myapp.views import  HomeSection,BlogSection,AboutSection
urlpatterns = [
    path('home/', HomeSection),
    path('blog/', BlogSection),
    path('about/', AboutSection),

]