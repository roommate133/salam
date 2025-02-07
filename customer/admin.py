from django.contrib import admin
from .models import Contact
@admin.register(Contact)

class ContactAdmin(admin.ModelAdmin):
    fields=['created','name','email','subject','message']
    readonly_fields=['created']
