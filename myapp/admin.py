from django.contrib import admin
from .models import Contact

# Register your models here.

#This connects the form in admin and the form in the html remember that

class ContactAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email_address', 'phone_number', 'message','date')
    list_filter = ('is_finished',)

'''    actions = ['mark_as_finished', 'mark_as_unfinished']
   
   
   # This is for the finished
    def mark_as_finished(self, request, queryset):
        queryset.update(is_finished=True)
    mark_as_finished.short_description = "Mark selected contacts as finished"

    def mark_as_unfinished(self, request, queryset):
        queryset.update(is_finished=False)
    mark_as_unfinished.short_description = "Mark selected contacts as unfinished"
'''

admin.site.register(Contact, ContactAdmin)
        


