from datetime import date
from django.db import models
from django.template.defaultfilters import slugify


class Campos(models.Model):
    menu_uno = models.CharField(max_length=50)
    menu_dos = models.CharField(max_length=50)
    menu_tres = models.CharField(max_length=50)
    imagen_ppal = models.ImageField(upload_to='media/')
    titulo_uno = models.CharField(max_length=100)
    parrafo_uno = models.CharField(max_length=500)
    imagen_uno = models.ImageField(upload_to='media/')
    frase_uno = models.CharField(max_length=100)
    img_des_uno = models.ImageField(upload_to='media/')
    titulo_des_uno = models.CharField(max_length=50)
    descripcion_uno = models.CharField(max_length=250)
    img_des_dos = models.ImageField(upload_to='media/')
    titulo_des_dos = models.CharField(max_length=50)
    descripcion_dos = models.CharField(max_length=250)
    img_des_tres = models.ImageField(upload_to='media/')
    titulo_des_tres = models.CharField(max_length=50)
    descripcion_tres = models.CharField(max_length=250)
    imagen_dos = models.ImageField(upload_to='media/')
    frase_dos = models.CharField(max_length=100)
    twitter = models.CharField(max_length=100)
    google = models.CharField(max_length=100)
    facebook = models.CharField(max_length=100)
    instagram = models.CharField(max_length=100)

    def __str__(self):
        return str(self.pk)

class Post(models.Model):
    titulo = models.CharField(max_length=140)
    resumen = models.CharField(max_length=500)
    imagen = models.ImageField(upload_to='media/')
    contenido = models.TextField()
    archivo = models.FileField(upload_to='media/', null=True, blank=True)
    date = models.DateField(default=date.today())
    slug = models.SlugField(blank= True)

    def __str__(self):
        return self.titulo

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.titulo)

        super(Post, self).save(*args, **kwargs)
