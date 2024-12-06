from django.contrib import admin
from .models import Post
# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')  # Поля, которые будут видны в админке
    search_fields = ['title']               # Поиск по полю 'title'
