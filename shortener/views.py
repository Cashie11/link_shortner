from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
import random
import string

def index(request):
    from .models import ShortURL  # Import inside the view function
    if request.method == 'POST':
        url = request.POST['url']
        short_url = ShortURL(url=url)
        short_url.save()
        shortened_url = request.build_absolute_uri('/') + short_url.short_code
        return render(request, 'index.html', {'shortened_url': shortened_url})
    return render(request, 'index.html')

def redirect_original(request, short_code):
    from .models import ShortURL  # Import inside the view function
    short_url = get_object_or_404(ShortURL, short_code=short_code)
    return redirect(short_url.url)

def generate_short_code():
    characters = string.ascii_letters + string.digits
    code = ''.join(random.choices(characters, k=6))
    return code


