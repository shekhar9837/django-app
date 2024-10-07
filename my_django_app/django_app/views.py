from django.shortcuts import render, get_object_or_404
from .models import chaiVarity
# Create your views here.

def django_app(request):
    chais = chaiVarity.objects.all()
    return render(request, 'django_app/django_app.html', {'chais': chais})

def chai_detail(request, chai_id):
    chai = get_object_or_404(chaiVarity, pk=chai_id)
    return render(request, 'django_app/chai_detail.html', {'chai': chai})