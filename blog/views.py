from django.shortcuts import render

def view_func (request):
    return render(request, "home.html")
