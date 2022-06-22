from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def demo(request):
    return render(request,"index.html")
def about(request):
    return render(request,"about.html")
def gallery(request):
    return render(request,"gallery.html")
def contact(request):
    return render(request,"contact.html")
def single(request):
    return render(request,"single-post.html")