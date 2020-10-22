from django.contrib import admin

from .models import Question, Choice, Sneakerstype, Sneakers

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Sneakerstype)
admin.site.register(Sneakers)