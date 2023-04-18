from django.shortcuts import render

def Base(request):
    return render(request, 'products/base.html')