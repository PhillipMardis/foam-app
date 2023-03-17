from django.shortcuts import render, redirect
from app.forms import *
from app.models import *
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def signupView(request):
    form = create_userForm()

    if request.method == "POST":
        form = create_userForm(request.POST)
        if form.is_valid():
            form.save()

    context = {"form": form}
    return render(request, "signup.html", context)


def loginView(request):
    context = {}
    return render(request, "login.html", context)


def homeView(request):
    return render(request, "home.html")


def postView(request):
    if request.method == "POST":
        form = postForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your item has been posted.")
            return redirect("home")
    form = postForm()
    return render(request, "post_item.html", {"form": form})


def buyView(request):
    items = postModel.objects.all()

    if request.method == "POST":
        form = buyForm(request.POST)
        return render(request, "buy.html", {"form": form, "items": items})

    form = buyForm()
    return render(request, "buy.html", {"form": form, "items": items})


def purchaseView(request, pk):
    item = postModel.objects.get(id=pk)
    return render(request, "purchase.html", {"item": item})


def successful_purchaseView(request, pk):
    item = postModel.objects.get(id=pk)
    item.delete()
    messages.success(request, "Item purchased!")
    return redirect("home")


def updateView(request, pk):
    item = postModel.objects.get(id=pk)
    form = postForm(instance=item)

    if request.method == "POST":
        form = postForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, "Your item has been updated.")
            return redirect("home")

    return render(request, "update.html", {"form": form, "item": item})


def deleteView(request, pk):
    item = postModel.objects.get(id=pk)
    return render(request, "delete.html", {"item": item})


def successful_deleteView(request, pk):
    item = postModel.objects.get(id=pk)
    item.delete()
    messages.success(request, "Item has been deleted.")
    return redirect("home")


def allusersView(request):
    ...
