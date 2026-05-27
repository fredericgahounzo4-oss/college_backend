# TCHEP College - Projet Django Complet

Frontend HTML/CSS/JS + Backend Django (remplacement complet du PHP).

## 🚀 Démarrage rapide

```bash
# 1. Installer les dépendances Python
pip install django pillow

# 2. Démarrer le serveur (depuis ce dossier)
python manage.py runserver 8000
# ou
./start.sh
```

**Ouvrir :** http://localhost:8000

---

## 🌐 Pages accessibles

| URL | Description |
|-----|-------------|
| http://localhost:8000/ | Page d'accueil |
| http://localhost:8000/about.html | À propos |
| http://localhost:8000/contact.html | Contact |
| http://localhost:8000/Registre.html | Formulaire d'inscription |
| http://localhost:8000/students-life.html | Vie étudiante |
| http://localhost:8000/news.html | Actualités |
| http://localhost:8000/events.html | Événements |
| http://localhost:8000/formations.html | Formations |
| http://localhost:8000/virtual-tour.html | Visite virtuelle |
| http://localhost:8000/alumni.html | Anciens élèves |

---

## 🔐 Administration

| Interface | URL | Login | Mot de passe |
|-----------|-----|-------|--------------|
| Calendrier des rentrées | /forms/admin-login/ | admin | admin123 |
| Galerie photos | /forms/admins-login/ | admin | admin123 |
| Django Admin (superuser) | /django-admin/ | (créer ci-dessous) |

**Créer un superuser Django Admin :**
```bash
python manage.py createsuperuser
```

---

## 📁 Structure du projet

```
college_backend/
├── start.sh                    ← Script de démarrage
├── manage.py
├── db.sqlite3                  ← Base de données (prête à l'emploi)
├── uploads/                    ← Photos galerie uploadées
│
├── College_frontend/           ← Tout le frontend (HTML + assets)
│   ├── index.html
│   ├── contact.html
│   ├── Registre.html
│   ├── assets/                 ← CSS, JS, images
│   └── ...
│
├── college_backend/            ← Configuration Django
│   ├── settings.py
│   └── urls.py
│
├── core/                       ← Application Django
│   ├── models.py               ← 6 modèles base de données
│   ├── views.py                ← Toutes les vues
│   ├── urls.py                 ← Routes
│   └── admin.py
│
└── templates/core/             ← Templates Django (pages admin)
    ├── admin_login.html
    ├── calendrier_admin.html
    ├── calendrier_public.html
    ├── dashboard.html
    └── ...
```

---

## 🔄 Équivalences PHP → Django

| Ancien PHP | Django |
|---|---|
| forms/config.php | settings.py (base de données) |
| forms/admin-login.php | /forms/admin-login/ |
| forms/calendrier-admin.php | /forms/calendrier-admin/ |
| forms/ajouter-date.php | /forms/ajouter-date/ (POST) |
| forms/delete-date.php?id=X | /forms/delete-date/X/ |
| forms/calendrier-public.php | /forms/calendrier-public/ |
| forms/admins-login.php | /forms/admins-login/ |
| forms/dashboard1.php | /forms/dashboard/ |
| forms/upload.php | /forms/upload-photo/ (POST) |
| forms/delete5.php?id=X | /forms/delete-photo/X/ |
| forms/student-activities.php | /forms/student-activities/ |
| forms/contact.php | /forms/contact/ (AJAX POST) |
| forms/contact1.php | /forms/inscription/ (AJAX POST) |
| forms/read.php | /forms/contacts/ |
| forms/read1.php | /forms/inscriptions/ |
| forms/update.php?id=X | /forms/contact/update/X/ |
| forms/update1.php?id=X | /forms/inscription/update/X/ |
| forms/delete.php?id=X | /forms/contact/delete/X/ |
| forms/delete1.php?id=X | /forms/inscription/delete/X/ |
| forms/logout.php | /forms/admin-logout/ |
| forms/logout5.php | /forms/admins-logout/ |

---

## 🗄️ Passer à MySQL (optionnel)

Dans `college_backend/settings.py`, remplacer le bloc DATABASES :

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'tchep_consulting',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

Puis :
```bash
pip install mysqlclient
python manage.py migrate
```

---

## ✅ Fonctionnalités

- ✅ Formulaire de contact (AJAX, sans rechargement de page)
- ✅ Formulaire d'inscription multi-étapes (AJAX)
- ✅ Calendrier des rentrées (admin protégé par session)
- ✅ Galerie photos (upload/suppression, admin protégé)
- ✅ Galerie publique des activités étudiantes
- ✅ Interface Django Admin complète
- ✅ Base de données SQLite incluse et prête
