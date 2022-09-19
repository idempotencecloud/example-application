from django.contrib import admin

# Register your models here.
from .models import Company,Individual

admin.site.register(Company)
admin.site.register(Individual)
