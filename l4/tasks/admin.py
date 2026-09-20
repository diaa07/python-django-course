from django.contrib import admin

from .models import Task
# Register your models here.


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'done', 'created_at', 'category')
    list_filter = ('title', 'done')
    search_fields = ('title',)
    readonly_fields = ('created_at',)
    list_editable = ('done',)
