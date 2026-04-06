from django.contrib import admin
from .models import TodoItem

# Register your models here.
admin.site.register(TodoItem)

class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'task', 'completed')
    search_fields = ('task',)
    list_filter = ('completed',)
    ordering = ('-id',)
    list_editable = ('completed',)
