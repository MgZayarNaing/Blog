from django.contrib import admin
from .models import HomeModel,BlogModel,AboutModle,ContactModel
# Register your models here.

admin.site.register(HomeModel)
admin.site.register(BlogModel)
admin.site.register(AboutModle)
admin.site.register(ContactModel)