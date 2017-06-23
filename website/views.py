from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'website/index.html', context={
                      'title': '命运石之门的选择', 
                      'welcome': 'Welcome to Steins;Gate'
                  })