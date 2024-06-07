
import requests
from django.shortcuts import render
from .models import Repository

def home(request):
    return render(request, 'home.html')

def fetch_repositories(request):
    access_token = request.GET.get('access_token')
    if access_token:
        headers = {'Authorization': f'token {access_token}'}
        response = requests.get('https://api.github.com/user/repos', headers=headers)
        if response.status_code == 200:
            repositories = response.json()
            return render(request, 'home.html', {'repositories': repositories})
        else:
            error_message = f'Failed to fetch repositories. Status code: {response.status_code}'
    else:
        error_message = 'Access token is required.'
    
    return render(request, 'home.html', {'error_message': error_message})
