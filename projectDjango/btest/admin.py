# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Pharmacy, Category, Medicine, AvailabilityOfMedicines

admin.site.register(Pharmacy)
admin.site.register(Category)
admin.site.register(Medicine)
admin.site.register(AvailabilityOfMedicines)

