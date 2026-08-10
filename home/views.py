from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages




def homeview(request):
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

  return render(request, 'home/index.html', {'form':form})