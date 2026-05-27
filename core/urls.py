from django.urls import path
from . import views

urlpatterns = [
    # ── Calendrier Admin ──────────────────────────────
    path('admin-login/', views.admin_login, name='admin_login'),
    path('admin-logout/', views.admin_logout, name='admin_logout'),
    path('calendrier-admin/', views.calendrier_admin, name='calendrier_admin'),
    path('ajouter-date/', views.ajouter_date, name='ajouter_date'),
    path('delete-date/<int:pk>/', views.delete_date, name='delete_date'),
    path('calendrier-public/', views.calendrier_public, name='calendrier_public'),

    # ── Galerie Admin ─────────────────────────────────
    path('admins-login/', views.admins_login, name='admins_login'),
    path('admins-logout/', views.admins_logout, name='admins_logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('upload-photo/', views.upload_photo, name='upload_photo'),
    path('delete-photo/<int:pk>/', views.delete_photo, name='delete_photo'),

    # ── Galerie publique ──────────────────────────────
    path('student-activities/', views.student_activities, name='student_activities'),

    # ── Contact ───────────────────────────────────────
    path('contact/', views.contact, name='contact'),
    path('contacts/', views.read_contacts, name='read_contacts'),
    path('contact/update/<int:pk>/', views.update_contact, name='update_contact'),
    path('contact/delete/<int:pk>/', views.delete_contact, name='delete_contact'),

    # ── Inscriptions ──────────────────────────────────
    path('inscription/', views.inscription, name='inscription'),
    path('inscriptions/', views.read_inscriptions, name='read_inscriptions'),
    path('inscription/update/<int:pk>/', views.update_inscription, name='update_inscription'),
    path('inscription/delete/<int:pk>/', views.delete_inscription, name='delete_inscription'),
]
