from django.shortcuts import render

def show_image(request):
    return render(request, 'page.html')

def menu(request):
    return render(request, 'menu.html')
