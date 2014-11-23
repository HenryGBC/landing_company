from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views.generic import DetailView, FormView, ListView, DeleteView
from landing.forms import LoginForm
from landing.models import Campos, Post


def home(request):
    campos = get_object_or_404(Campos, pk=1)
    template = 'index.html'
    return render(request, template, locals())

def inicio(request):
    template = 'inicio.html'
    if request.method == 'POST':
        usuario = request.POST['username']
        clave = request.POST['password']
        log = False
        user = authenticate(username=usuario, password=clave)
        if user is not None:
            # the password verified for the user
            if user.is_active:
                print("User is valid, active and authenticated")
                login(request, user)
                return HttpResponseRedirect('/inicio/')
            else:
                print("The password is valid, but the account has been disabled!")
        else:
                # the authentication system was unable to verify the username and password
            print("The username and password were incorrect.")
            log = True
            return  render(request, template, locals())
    return render(request, template, locals())

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/inicio/')

def crear(request):
    template = 'crear.html'
    if request.user.is_authenticated():
        if request.method == 'POST' and request.POST["titulo"]:
            titulo = request.POST["titulo"]
            resumen = request.POST["resumen"]
            contenido = request.POST["parrafo"]
            if titulo and resumen and contenido :
                P = Post(titulo=titulo, resumen=resumen, imagen=request.FILES.get('imagen', False ), contenido=contenido, archivo=request.FILES.get('archivo', False ))
                P.save()
                return HttpResponseRedirect('/posts/')
            else:
                print "incompletos brother"
    else:
        if request.method == 'POST' and request.POST["username"]:
            usuario = request.POST['username']
            clave = request.POST['password']
            log = False
            user = authenticate(username=usuario, password=clave)
            if user is not None:
                # the password verified for the user
                if user.is_active:
                    print("User is valid, active and authenticated")
                    login(request, user)
                    return HttpResponseRedirect('/crear/')
                else:
                    print("The password is valid, but the account has been disabled!")
            else:
                # the authentication system was unable to verify the username and password
                print("The username and password were incorrect.")
                log = True
                return  render(request, template, locals())



    return render(request, template, locals())



class PostsView(ListView):
    model = Post
    template_name = 'posts.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'post.html'


def delete(request, id):
    post = get_object_or_404(Post, pk=id)
    post.delete()
    return HttpResponseRedirect('/posts/')


def editar(request, id):
    template ="edit.html"
    post = get_object_or_404(Post, pk=id)
    if request.method == 'POST':
        post.titulo=request.POST['titulo']
        post.resumen=request.POST['resumen']
        post.contenido=request.POST['parrafo']

        if request.FILES.get('imagen', False ):
            post.imagen = request.FILES.get('imagen', False)
        if request.FILES.get('archivo', False ):
            post.archivo = request.FILES.get('archivo', False)


        post.save()
        return HttpResponseRedirect('/posts/')

    return render(request, template, locals())