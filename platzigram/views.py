from django.http import HttpResponse
import pdb

def hello_world(request):
    return HttpResponse('Hello, world!')

def hi(request):
    pdb.set_trace()
    return HttpResponse('Hi!')