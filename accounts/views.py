from django.shortcuts import render, redirect
from .forms import (
    UserRegisterForm,
    UserUpdateForm,
    ProfileUpdateForm,
    )
from django.contrib.auth import authenticate,login
from django.contrib import messages

# class RegisterView(UserRegisterForm):
#     template_name = "register.html"
#     form_class = UserRegisterForm
#     def form_valid(self, form):
#         form.save()
#         username = form.cleaned_data.get("username")
#         password = form.cleaned_data.get("password1")
#         messages.info(f'Hey {username}, We are glad to see you here!Try our tutorials!')
#         user = authenticate(username=username, password=password)
#         login(request, user)
#         return redirect("courses")

        
def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            messages.info(request, f'Hey {username}, We are glad to see you here!Try our tutorials!')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect("courses")
    else:
        form = UserRegisterForm()
    context = {
        'form':form
    }
    return render(request, 'register.html', context)

def profile (request):
    if request.method=="POST":
        u_form = UserUpdateForm( request.POST, instance=request.user)
        p_form = ProfileUpdateForm( request.POST, request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form':u_form,
        'p_form':p_form,
    }
    return render(request, "profile.html", context)
    
