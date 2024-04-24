from django.shortcuts import render
from .models import form_contact

# Create your views here.

def index(request):
    return render(request, 'index.html')


def contact(request):
    messages = ""
    if request.method == 'POST':
     nom = request.POST.get('nom')
     sujet = request.POST.get('sujet')
     email= request.POST.get('email')
     telephone=request.POST.get('telephone')
     message = request.POST.get('message')
     formul= form_contact.objects.create(nom=nom, sujet=sujet, email=email, message=message, telephone=telephone)
     formul.save()
     messages= "Nous avons réçu votre message,nous vous contacterons "
    return render(request, 'contact.html',{"messages":messages})

def about(request):
    return render(request, 'about-us.html')

def service(request):
    return render(request, 'blog-grid-sidebar.html')