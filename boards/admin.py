from django.contrib import admin
import boards.models 
from django.contrib.auth.models import	User

# Register your models here.
admin.site.register(boards.models.Board)

