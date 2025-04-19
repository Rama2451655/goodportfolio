from django.shortcuts import render, redirect
from .models import Project
from .forms import ContactForm

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects.html', {'projects': projects})

def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('contact')
    return render(request, 'contact.html', {'form': form})
from .models import Testimonial

def testimonials(request):
    feedbacks = Testimonial.objects.all().order_by('-date')
    return render(request, 'main/testimonials.html', {'feedbacks': feedbacks})
