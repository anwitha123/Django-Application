from django.shortcuts import render

# # Create your views here.
# from django.http import JsonResponse

# def hello_world(request):
#     return JsonResponse({"Message": "Hello World!"})

from django.shortcuts import render

def hello_world(request):
    context = {"message": "Hello World!"}
    return render(request, 'hello_world.html', context)
