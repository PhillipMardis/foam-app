from django.shortcuts import render, redirect
from app.forms import *
from django.contrib import messages

# Create your views here.
def homeView(request):
    return render(request, "home.html")


def postView(request):
    if request.method == "POST":
        form = postForm(request.POST)
        if form.is_valid():
            # name = form.cleaned_data["name"]
            # desc = form.cleaned_data["desc"]
            # cond = form.cleaned_data["cond"]
            # price = form.cleaned_data["price"]
            form.save()
            messages.success(request, "Your item has been posted.")
            return redirect("home")
    else:
        form = postForm()
        return render(request, "post_item.html", {"form": form})


def signupView(request):
    ...


def loginView(request):
    ...


def buyView(request):
    ...


def allusersView(request):
    ...
