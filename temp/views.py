from django.shortcuts import render, redirect
from .models import *
from .forms import ContactForm


# --------------VIEWS-------------------

def index(request):
    post = Post.objects.all()
    context = {
        'post' : post
    }
    return render(request,
                  template_name='index.html',
                  context=context)

def about(request):
    return render(request,
                  template_name='about.html')

def contact(request):
    return render(request,
                  template_name='contact.html')

def videos(request):
    return render(request,
                  template_name='videos.html')




# --------------DETAILS-------------------

def photo_detail(request, id):
    post = Post.objects.get(pk=id)
    posts = Post.objects.all()
    context = {
        'post' : post,
        'posts' : posts
    }
    return render(request,
                  template_name='photo-detail.html',
                  context=context)

def video_detail(request, id):
    return render(request,
                  template_name='video_detail.html')


# --------------CREATES-------------------

def add_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request,
                  'contact.html',
                  context={'form': form})




















