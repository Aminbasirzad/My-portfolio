from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages
from .models import Skils, Resume, About
from .mongo import projects




def homeview(request):
  projects_data = projects.find()
  resume = Resume.objects.first()
  about = About.objects.first()
  if request.method == 'POST':
    form = ContactForm(request.POST)

    if form.is_valid():
      form.save()
      messages.success(request, 'Your message has been sent successfully.')
      return redirect('home:homeview')
    else:
      messages.error(request, 'Your message could not be sent.')

  else:
    form = ContactForm()

  skils = Skils.objects.all()

  return render(request, 'home/index.html', {
    'form':form, 'skils':skils,
    "projects":projects_data,
    "resume":resume,
    'about':about,
  })

