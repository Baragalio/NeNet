from django.shortcuts import render

def main_str(request):
    return render(request, 'main.html')