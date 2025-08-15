# myapp/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactSubmission
from django.urls import reverse


def Portfolio(request):
    return render(request, "index.html")


def contact_view(request):
    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            message = request.POST.get('message')

            ContactSubmission.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )

            messages.success(request, 'Your message has been sent successfully!')
            return redirect(reverse('Portfolio') + '#contact')

        except Exception as e:
            messages.error(request, f'An error occurred: {str(e)}')
            return redirect(reverse('Portfolio') + '#contact')

    return redirect(reverse('Portfolio') + '#contact')

def contact_list(request):
    contacts = ContactSubmission.objects.all()
    return render(request, "register.html", {"contacts": contacts})