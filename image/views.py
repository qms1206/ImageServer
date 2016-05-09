from django.shortcuts import render
from django.template import loader,Context
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.http import HttpResponse
from   PIL import Image
from image.forms import PictureForm

def upload(request):
    print('upload')
    if request.method == 'POST':
        print('post')
        reqfile = request.FILES['picfile']
        img = Image.open(reqfile)
        # img.thumbnail((500, 500), Image.ANTIALIAS)
        img.save("h:/a.png", "png")
        return HttpResponse('ok!');

def init(request):
    print('req')
    return render_to_response('index.html')