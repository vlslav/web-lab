from .models import AvailabilityOfMedicines
from django.shortcuts import render


def index(request):
    bbs = AvailabilityOfMedicines.objects.all()
    return render(request, "proj/index.html", {'bbs': bbs})
