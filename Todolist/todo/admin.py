from django.contrib import admin

from .models import ToDo, Status, Priority


class ToDoAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'will_end', 'priority',
                    'status', 'name', 'description')
    readonly_fields = ('id', 'created_at')

    save_on_top = True


class StatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class PriorityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


admin.site.register(ToDo, ToDoAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(Priority, PriorityAdmin)
