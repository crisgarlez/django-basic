from django.http import HttpResponse
import json

def hello_world(request):
    return HttpResponse('Hello, world!')

def sorted_integers(request):
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sorted_ints = sorted(numbers)
    data = {
        "status": "ok",
        "numbers": sorted_ints,
        "message": "Success"
    }
    return HttpResponse(json.dumps(data), content_type='application/json')

def hi(request, name, age):
    return HttpResponse(f'Hello, {name} ! you have {age} years old');