from django.shortcuts import render, render_to_response
from django.http import HttpResponse
import os

# Create your views here.

def file_upload(request):
    return render(request, 'file_upload_hide_input_with_function.html')
    

def upload(request):
    f = request.FILES['upload_file']
    filename = f.name
    with open('upload\\{}'.format(filename), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    
    # do something with the file uploaded
    report = '<h1>UPLOADED FILE：{}</h1><h2>REPORT FROM FILE CONTENTS</h2>'.format(filename)
    
    #return HttpResponse()
    return render_to_response('report.html', {'report': report})