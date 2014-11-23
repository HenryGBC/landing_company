from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.
from landing.models import Campos, Post

@admin.register(Post)
class PostModelAdmin(SummernoteModelAdmin):
	pass

admin.site.register(Campos)



