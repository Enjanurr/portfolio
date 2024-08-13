from django.contrib import admin
from .models import Contact

# Register your models here.

#This connects the form in admin and the form in the html remember that
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email_address', 'phone_number', 'message')
    
'''
@admin.register(Comment)  # short hand notation for admin.site.register()
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)
'''
        


