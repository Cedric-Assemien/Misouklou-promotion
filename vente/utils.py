from django.template.loader import render_to_string
from django.core.mail import EmailMessage

def email_template (sujet1,template_name,context, email_user:list,email_init):
    
    message1= render_to_string(template_name,context)
    
    email = EmailMessage(
        sujet1,
        message1,
        email_init,
        email_user,
    )
    email.send()
    
    return True
    
    

