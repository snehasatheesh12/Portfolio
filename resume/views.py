from django.shortcuts import render,redirect
from.models import *
from django.conf import settings
from django.core import mail
from django.contrib import messages
from django.http import FileResponse, Http404
import os

def home(request):
     return render(request,'index.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        project = request.POST.get('project')

    
        from_email = settings.EMAIL_HOST_USER

        email_message = mail.EmailMessage(
            subject=f'Email is from {name}',
            body=f'User Email: {email}\nUser Phone: {phone}\n\n\nQuery:\n{message}',
            from_email=from_email,
            to=['snehasatheesh176@gmail.com']  
        )
        try:
            email_message.send()
            messages.success(request, 'Your message has been sent successfully! Thank you.')
        except Exception as e:
            messages.error(request, f'An error occurred while sending the email: {e}')
        
        confirmation_message = mail.EmailMessage(
            subject='Thank you for contacting us',
            body=f'Hello {name},\n\nThank you for reaching out to us. We have received your message and will get back to you soon.',
            from_email=from_email,
            to=[email]
        )
        try:
            confirmation_message.send()
        except Exception as e:
            messages.error(request, f'An error occurred while sending the confirmation email: {e}')

        return redirect('home')



def download_cv(request):
    file_path = os.path.join('static', 'resume', 'SNEHA.pdf')
    
    if os.path.exists(file_path):
        return FileResponse(open(file_path, 'rb'), as_attachment=True, filename='SNEHA.pdf')
    else:
        raise Http404("File not found")