from django.shortcuts import render

# Create your views here.

def django_app(request):
    return render(request, 'django_app/django_app.html')