from django.shortcuts import render

def home(request):
    return render(request, 'core/index.html')
def about(request):
    return render(request, 'core/about_section.html')
def services(request):
    return render(request, 'core/services_page.html')
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactInquiry

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Save into the database table
        ContactInquiry.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        
        # Display a success message banner
        messages.success(request, "Your message has been safely sent!")
        return redirect('contact')

    return render(request, 'core/contact_section.html')

def projects(request):
    return render(request, 'core/project_section.html')


