from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from myapp.models import Customer
# from django.views import View
# from django.template.loader import get_template

def sendanemail(request):
      if request.method =='POST':
          name = request.POST.get('message_name')
          number =request.POST.get('message_number')
          Email =request.POST.get('message_email')
          message =request.POST.get('message') 
      
          html_content=render_to_string("emailtemp.html",{'message_name':name,'message_email':Email,'message':message,'message_number':number})
          text_content=strip_tags(html_content)
          email= EmailMultiAlternatives(
                  "contact form", 
                   text_content,
                   settings.EMAIL_HOST_USER,
                        ['p86650158@gmail.com'],
                  )
          email.attach_alternative(html_content,"text/html")
          email.send()
      return render(request, 'myapp/try.html')

     