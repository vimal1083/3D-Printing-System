# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from models import Companies, Price

class CompanieAdmin(admin.ModelAdmin):
     model= Companies
     filter_horizontal = ('materials','prices') #If you don't specify this, you will get a multiple select widget.

admin.site.register(Price)
admin.site.register(Companies, CompanieAdmin)