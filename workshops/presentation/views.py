from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
  template = loader.get_template('presentation/index.html')
  context = {
      'foo': ['hello world'],
  }
  return HttpResponse(template.render(context, request))
