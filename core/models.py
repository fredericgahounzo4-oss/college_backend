from django.db import models

class Admin(models.Model):
    """Table admin (calendrier) - connexion MD5 comme l'ancien PHP"""
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=255)
    class Meta:
        db_table = 'admin'
    def __str__(self):
        return self.username

class Admins(models.Model):
    """Table admins (galerie photos)"""
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=255)
    class Meta:
        db_table = 'admins'
    def __str__(self):
        return self.username

class Calendrier(models.Model):
    """Dates de rentrée"""
    date_rentree = models.DateField()
    description = models.CharField(max_length=255, blank=True, default='')
    class Meta:
        db_table = 'calendrier'
        ordering = ['date_rentree']
    def __str__(self):
        return str(self.date_rentree)

class Contact(models.Model):
    """Messages de contact"""
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'contacts'
        ordering = ['-created_at']
    def __str__(self):
        return f"{self.name} - {self.subject}"

class Inscription(models.Model):
    """Inscriptions étudiants"""
    prenom = models.CharField(max_length=100)
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    telephone = models.CharField(max_length=20, blank=True, default='')
    date_naissance = models.DateField(null=True, blank=True)
    adresse = models.TextField(blank=True, default='')
    niveau_etudes = models.CharField(max_length=100, blank=True, default='')
    categorie = models.CharField(max_length=100, blank=True, default='')
    programme = models.CharField(max_length=200, blank=True, default='')
    session = models.CharField(max_length=100, blank=True, default='')
    type_formation = models.CharField(max_length=100, blank=True, default='')
    source = models.CharField(max_length=100, blank=True, default='')
    situation = models.CharField(max_length=100, blank=True, default='')
    objectifs = models.TextField(blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'inscriptions'
        ordering = ['-created_at']
    def __str__(self):
        return f"{self.prenom} {self.nom}"

class Gallery(models.Model):
    """Galerie photos - stockage via Cloudinary"""
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='gallery/')  # stocké sur Cloudinary
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'gallery'
        ordering = ['-created_at']
    def __str__(self):
        return self.title
