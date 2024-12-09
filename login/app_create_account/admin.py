from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(User)
admin.site.register(Horta)
admin.site.register(HortaNutriente)
admin.site.register(Job)
admin.site.register(Document)

