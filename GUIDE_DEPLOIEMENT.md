# 🚀 Guide de déploiement — GitHub + Render

## Ce qui a été modifié dans ton projet

| Fichier | Modification |
|---|---|
| `settings.py` | Variables d'env, WhiteNoise pour les statics, DEBUG=False en prod |
| `requirements.txt` | Ajouté : gunicorn, whitenoise, python-decouple |
| `render.yaml` | Configuration automatique pour Render |
| `.gitignore` | Exclut db.sqlite3, uploads/, .env, __pycache__ |
| `.env.example` | Modèle pour les variables d'environnement |

---

## ÉTAPE 1 — Préparer Git en local

Ouvre un terminal dans le dossier `college_backend/` (là où se trouve `manage.py`) :

```bash
cd college_backend

# Initialiser git
git init

# Ajouter tous les fichiers (le .gitignore exclut automatiquement db.sqlite3 etc.)
git add .

# Premier commit
git commit -m "Initial commit - TCHEP College Django backend"
```

---

## ÉTAPE 2 — Créer le dépôt GitHub

1. Va sur **https://github.com/new**
2. Nom du dépôt : `college-backend` (ou ce que tu veux)
3. Laisse en **Public** (nécessaire pour le plan gratuit Render) ou **Private**
4. **Ne coche rien** (pas de README, pas de .gitignore — tu les as déjà)
5. Clique **Create repository**

GitHub t'affiche alors des commandes. Exécute dans ton terminal :

```bash
git remote add origin https://github.com/TON_USERNAME/college-backend.git
git branch -M main
git push -u origin main
```

Remplace `TON_USERNAME` par ton nom d'utilisateur GitHub.

---

## ÉTAPE 3 — Déployer sur Render

### 3a. Créer un compte Render
Va sur **https://render.com** → "Get Started for Free" → connecte-toi avec GitHub (plus simple).

### 3b. Créer un nouveau Web Service
1. Dashboard Render → **New +** → **Web Service**
2. Connecte ton dépôt GitHub `college-backend`
3. Render va détecter le `render.yaml` automatiquement

### 3c. Configurer le service manuellement (si render.yaml non détecté)

| Champ | Valeur |
|---|---|
| **Runtime** | Python 3 |
| **Build Command** | `pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate` |
| **Start Command** | `gunicorn college_backend.wsgi:application --bind 0.0.0.0:$PORT` |

### 3d. Variables d'environnement (obligatoire !)

Dans Render → ton service → **Environment** → ajouter :

| Clé | Valeur |
|---|---|
| `SECRET_KEY` | Clique "Generate" pour en créer une aléatoire |
| `DEBUG` | `False` |
| `ALLOWED_HOSTS` | `ton-app.onrender.com` (Render te donne l'URL) |

### 3e. Lancer le déploiement
Clique **Create Web Service** → Render build et démarre automatiquement.

⏳ Premier déploiement : 3-5 minutes.

---

## ÉTAPE 4 — Vérifier que ça marche

Ton app sera accessible à l'URL donnée par Render (ex: `https://college-backend-xxxx.onrender.com`).

Pages à tester :
- `/` → Page d'accueil
- `/forms/calendrier-public/` → Calendrier public
- `/django-admin/` → Interface Django admin

---

## ⚠️ Points importants

### SQLite sur Render (plan gratuit)
Render utilise un **disque éphémère** : la base `db.sqlite3` est **réinitialisée à chaque redéploiement**. 

Pour conserver les données :
- **Option 1** : Utiliser le **Render Disk** (payant, ~$1/mois) → monte un volume persistant
- **Option 2** : Migrer vers **PostgreSQL** (Render offre 1 base Postgres gratuite !)

### Migrer vers PostgreSQL (recommandé)
Dans Render → **New +** → **PostgreSQL** → copie l'URL de connexion.

Puis dans `settings.py` remplace le bloc DATABASES par :
```python
import dj_database_url
DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL', default=f'sqlite:///{BASE_DIR / "db.sqlite3"}')
    )
}
```
Et ajoute `dj-database-url` dans `requirements.txt`.

### Photos uploadées (galerie)
Les fichiers uploadés dans `uploads/` sont aussi perdus à chaque redéploiement sur le plan gratuit.
Solution : utiliser **Cloudinary** ou **AWS S3** pour le stockage des médias.

---

## 🔄 Mises à jour futures

Pour mettre à jour ton app après modification du code :
```bash
git add .
git commit -m "Description de la modification"
git push origin main
```
Render redéploie automatiquement à chaque push sur `main`.

---

## 📞 Résumé des commandes

```bash
# 1. Dans le dossier du projet
git init
git add .
git commit -m "Initial commit"

# 2. Connecter à GitHub (remplace TON_USERNAME)
git remote add origin https://github.com/TON_USERNAME/college-backend.git
git branch -M main
git push -u origin main

# 3. Render se charge du reste via le dashboard
```
