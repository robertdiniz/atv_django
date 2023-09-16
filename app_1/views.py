from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse(f'Hello, world!<br><img src="https://pbs.twimg.com/media/EemEGxLXgAUz4eo.png" width="200px"><hr>')
