from django.contrib import admin
from .models import Project, Note

# class DateTime(models.Model):
#     datetime = models.DateTimeField(auto_now_add=True)
#     def __unicode__(self):
#         return unicode(self.datetime)

class ItemAdmin(admin.ModelAdmin):
    list_display = ["task", "date", "completed"]
    search_fields = ["task"]

class ItemInline(admin.TabularInline):
    model = Note

class DateAdmin(admin.ModelAdmin):
    list_display = ["date"]
    inlines = [ItemInline]

admin.site.register(Project)
admin.site.register(Note,ItemAdmin)