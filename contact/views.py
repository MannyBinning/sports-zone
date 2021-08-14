from django.shortcuts import render
from django.contrib import messages
from django.conf import settings

from .forms import ContactForm


def contact(request):
    """ Contact Us form """

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_message = {
                'full_name': request.POST['full_name'],
                'email': request.POST['email'],
                'message': request.POST['message'],
            }
            form.save()
            messages.success(request, 'Your message has been delivered. \
                A member of staff will get back to you shortly. Thank you.')
        else:
            messages.error(request, 'Message failed.  Please submit \
                a Valid form.')

    form = ContactForm()
    template = 'contact/contact.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
