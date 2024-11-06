from django.contrib import admin

# Register your models here.
from .models import Post  # Replace with your model name
admin.site.register(Post)