from django.contrib import admin
from .models import Userdata, Doctor, Sessiondata, Image

# Register your models here.

admin.site.register(Userdata)
admin.site.register(Doctor)
admin.site.register(Sessiondata)
admin.site.register(Image)

