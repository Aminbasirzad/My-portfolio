from django.contrib import admin
from .models import Contact, Skils, Resume, About

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
  list_display = ('name', 'email', 'subject', 'created_at')

  @admin.register(Skils)
  class SkilAdmin(admin.ModelAdmin):
    list_display = ('name', 'percentage')

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
  list_display = ['birth_date', 'phone', 'city', 'email', 'education', 'created_at']

  @admin.register(About)
  class AboutAdmin(admin.ModelAdmin):
    list_display = ['name','title' ,'description', 'image', 'quote']