from django.contrib import admin

from .models import Information

class InformationAdmin(admin.ModelAdmin):
    list_display = ['user', 'age', 'gender', 'color', 'season', 'scope', 'purpose', 'count_fr']

admin.site.register(Information, InformationAdmin)
