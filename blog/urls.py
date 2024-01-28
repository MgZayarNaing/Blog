from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

# admin customize
admin.site.site_title = "Blog"
admin.site.site_header = "MY BLOG"
admin.site.index_title = "BLOG"

urlpatterns = [
    path('', lambda request: redirect('/app/blog/')),
    path("admin/", admin.site.urls),
    path(("app/"), include("myapp.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)