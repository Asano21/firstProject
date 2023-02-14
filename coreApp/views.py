from django.shortcuts import render, get_object_or_404
from .models import Post, Character


def homePage(request):
    posts = Post.objects.all().order_by('-postDate')
    return render(request, 'home.html', {
        'posts' : posts
    })
def postDetail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post-detail.html', {
        'post':post
    })

def aboutPage(request):
    title = "About Page"
    return render(request, 'about.html', {
        'title': title,
    })

def heroPage(request):
    heroes = Character.objects.all().order_by('-name')
    return render(request, 'hero.html', {
        'heroes': heroes,
    })
def heroDetail(request, pk):
    hero = get_object_or_404(Character, pk=pk)
    return render(request, 'hero-detail.html', {
        'hero':hero
    })