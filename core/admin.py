from django.contrib import admin
from .models import Admin, Admins, Calendrier, Contact, Inscription, Gallery

@admin.register(Calendrier)
class CalendrierAdmin(admin.ModelAdmin):
    list_display = ('date_rentree', 'description')
    ordering = ('date_rentree',)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    ordering = ('-created_at',)

@admin.register(Inscription)
class InscriptionAdmin(admin.ModelAdmin):
    list_display = ('prenom', 'nom', 'email', 'programme', 'created_at')
    ordering = ('-created_at',)

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')

@admin.register(Admin)
class AdminModelAdmin(admin.ModelAdmin):
    list_display = ('username',)

@admin.register(Admins)
class AdminsModelAdmin(admin.ModelAdmin):
    list_display = ('username',)
