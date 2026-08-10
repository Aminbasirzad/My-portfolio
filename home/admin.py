from django.contrib import admin
from .models import Contact, Skils

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
  list_display = ('name', 'email', 'subject', 'created_at')

  @admin.register(Skils)
  class SkilAdmin(admin.ModelAdmin):
    list_display = ('name', 'percentage')