from django.shortcuts import render

from vente.utils import email_template
from .models import form_contact

from django.conf import settings
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
     messages= "Nous avons réçu votre méssage,vérifier votre mail svp"
     
     email_user = formul.email
     email_init= settings.EMAIL_HOST_USER
     template_name = "email.html"
     sujet1= "Confirmation de réception de votre méssage - Misouklou"
     context = {
        'nom':f"{formul.nom}",
        'sujet':f"{formul.sujet}"
       
     }
     email_template(sujet1,template_name,context,[email_user],email_init)

    return render(request, 'contact.html',{'messages':messages})

def about(request):
    return render(request, 'about-us.html')

def service(request):
    return render(request, 'blog-grid-sidebar.html')