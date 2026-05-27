import hashlib
import os
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from .models import Admin, Admins, Calendrier, Contact, Inscription, Gallery


# ─── Helpers ─────────────────────────────────────────────────────────────────

def md5_password(password):
    return hashlib.md5(password.encode()).hexdigest()

def admin_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.session.get('admin'):
            return redirect('admin_login')
        return view_func(request, *args, **kwargs)
    return wrapper

def admins_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.session.get('admins'):
            return redirect('admins_login')
        return view_func(request, *args, **kwargs)
    return wrapper


# ─── Admin Calendrier ─────────────────────────────────────────────────────────

def admin_login(request):
    error = ''
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        try:
            Admin.objects.get(username=username, password=md5_password(password))
            request.session['admin'] = True
            return redirect('calendrier_admin')
        except Admin.DoesNotExist:
            error = 'Identifiants incorrects'
    return render(request, 'core/admin_login.html', {'error': error})

def admin_logout(request):
    request.session.flush()
    return redirect('admin_login')

@admin_required
def calendrier_admin(request):
    dates = Calendrier.objects.all()
    return render(request, 'core/calendrier_admin.html', {'dates': dates})

@admin_required
@require_POST
def ajouter_date(request):
    date_rentree = request.POST.get('date_rentree', '').strip()
    description = request.POST.get('description', '').strip()
    if date_rentree:
        Calendrier.objects.create(date_rentree=date_rentree, description=description)
    return redirect('calendrier_admin')

@admin_required
def delete_date(request, pk):
    get_object_or_404(Calendrier, pk=pk).delete()
    return redirect('calendrier_admin')

def calendrier_public(request):
    dates = Calendrier.objects.all()
    return render(request, 'core/calendrier_public.html', {'dates': dates})


# ─── Admin Galerie ────────────────────────────────────────────────────────────

def admins_login(request):
    error = ''
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        try:
            Admins.objects.get(username=username, password=password)
            request.session['admins'] = True
            return redirect('dashboard')
        except Admins.DoesNotExist:
            error = 'Identifiants incorrects'
    return render(request, 'core/admins_login.html', {'error': error})

def admins_logout(request):
    request.session.pop('admins', None)
    return redirect('admins_login')

@admins_required
def dashboard(request):
    images = Gallery.objects.all()
    return render(request, 'core/dashboard.html', {'images': images})

@admins_required
@require_POST
def upload_photo(request):
    title = request.POST.get('title', '').strip()
    image_file = request.FILES.get('image')
    if image_file and title:
        ext = image_file.name.rsplit('.', 1)[-1].lower()
        if ext not in ['jpg', 'jpeg', 'png', 'gif']:
            return redirect('dashboard')
        Gallery.objects.create(title=title, image=image_file)
    return redirect('dashboard')

@admins_required
def delete_photo(request, pk):
    photo = get_object_or_404(Gallery, pk=pk)
    if photo.image and os.path.isfile(photo.image.path):
        os.remove(photo.image.path)
    photo.delete()
    return redirect('dashboard')

def student_activities(request):
    images = Gallery.objects.all()
    return render(request, 'core/student_activities.html', {'images': images})


# ─── Contact (csrf_exempt pour appel depuis HTML statique) ───────────────────

@csrf_exempt
@require_POST
def contact(request):
    name = request.POST.get('name', '').strip()
    email = request.POST.get('email', '').strip()
    subject = request.POST.get('subject', '').strip()
    message = request.POST.get('message', '').strip()
    if name and email:
        Contact.objects.create(name=name, email=email, subject=subject, message=message)
        return JsonResponse({'status': 'success', 'message': '✅ Votre message a été envoyé avec succès'}, json_dumps_params={'ensure_ascii': False})
    return JsonResponse({'status': 'error', 'message': 'Champs manquants'}, status=400, json_dumps_params={'ensure_ascii': False})

def read_contacts(request):
    contacts = Contact.objects.all()
    return render(request, 'core/read_contacts.html', {'contacts': contacts})

def update_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        contact.name    = request.POST.get('name', contact.name)
        contact.email   = request.POST.get('email', contact.email)
        contact.subject = request.POST.get('subject', contact.subject)
        contact.message = request.POST.get('message', contact.message)
        contact.save()
        return redirect('read_contacts')
    return render(request, 'core/update_contact.html', {'contact': contact})

def delete_contact(request, pk):
    get_object_or_404(Contact, pk=pk).delete()
    return redirect('read_contacts')


# ─── Inscriptions (csrf_exempt pour appel depuis HTML statique) ──────────────

@csrf_exempt
@require_POST
def inscription(request):
    data = {
        'prenom':         request.POST.get('prenom', ''),
        'nom':            request.POST.get('nom', ''),
        'email':          request.POST.get('email', ''),
        'telephone':      request.POST.get('telephone', ''),
        'adresse':        request.POST.get('adresse', ''),
        'niveau_etudes':  request.POST.get('niveau_etudes', ''),
        'categorie':      request.POST.get('categorie', ''),
        'programme':      request.POST.get('programme', ''),
        'session':        request.POST.get('session', ''),
        'type_formation': request.POST.get('type_formation', ''),
        'source':         request.POST.get('source', ''),
        'situation':      request.POST.get('situation', ''),
        'objectifs':      request.POST.get('objectifs', ''),
    }
    dob = request.POST.get('date_naissance', '').strip()
    if dob:
        data['date_naissance'] = dob
    Inscription.objects.create(**data)
    return JsonResponse({'status': 'success', 'message': 'Inscription enregistrée avec succès'}, json_dumps_params={'ensure_ascii': False})

def read_inscriptions(request):
    inscriptions = Inscription.objects.all()
    return render(request, 'core/read_inscriptions.html', {'inscriptions': inscriptions})

def update_inscription(request, pk):
    insc = get_object_or_404(Inscription, pk=pk)
    if request.method == 'POST':
        for field in ['prenom','nom','email','telephone','adresse','niveau_etudes',
                      'categorie','programme','session','type_formation','source','situation','objectifs']:
            setattr(insc, field, request.POST.get(field, getattr(insc, field)))
        dob = request.POST.get('date_naissance', '').strip()
        if dob:
            insc.date_naissance = dob
        insc.save()
        return redirect('read_inscriptions')
    return render(request, 'core/update_inscription.html', {'insc': insc})

def delete_inscription(request, pk):
    get_object_or_404(Inscription, pk=pk).delete()
    return redirect('read_inscriptions')


# ─── Serve Frontend Static Files ─────────────────────────────────────────────

from django.views.static import serve as static_serve
from django.conf import settings
import os

FRONTEND_DIR = os.path.join(settings.BASE_DIR, 'College_frontend')

def serve_frontend(request, path='index.html'):
    """Sert les fichiers HTML et assets du frontend."""
    if not path:
        path = 'index.html'
    return static_serve(request, path, document_root=FRONTEND_DIR)
