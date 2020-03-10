from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Session)
admin.site.register(Lead)
admin.site.register(Hostpot)