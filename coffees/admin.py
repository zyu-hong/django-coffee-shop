from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(OriginPlace)
admin.site.register(Mainprocessing)
admin.site.register(Coffee)
admin.site.register(Grinding)