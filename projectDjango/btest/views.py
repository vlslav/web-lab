from .models import AvailabilityOfMedicines
from django.shortcuts import render


def index(request):
    availabilityOfMedicines = AvailabilityOfMedicines.objects.all()
    return render(request, "pharmacy/index.html", {'bbs': availabilityOfMedicines})