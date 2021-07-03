from boring_website.forms import ContactForm
from django.contrib import admin
from .models import *

admin.site.register(ContactBox)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Review)
admin.site.register(ReviewElement)