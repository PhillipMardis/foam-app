from django.shortcuts import render, redirect
from app.forms import *
from app.models import *
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from app.decorators import *
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.


@unauthenticated_user
# @allowed_users(allowed_roles=["premium", "free"])
def signupView(request):
    form = CreateUserForm()
    if request.method == "POST":

        form = CreateUserForm(request.POST)
        if form.is_valid():

            form.save()

            username = form.cleaned_data.get("username")
            type = form.cleaned_data.get("type")

            user = User.objects.get(username=username)
            group = Group.objects.get(name=type)
            user.groups.add(group)

            messages.success(request, "Account created for " + user.username)
            return redirect("login")
        else:
            messages.error(request, "Passwords do not match")

    context = {"form": form}
    return render(request, "signup.html", context)


@unauthenticated_user
def loginView(request):
    form = loginForm()
    if request.method == "POST":
        form = loginForm(request, request.POST)

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Successfully logged in!")
                return redirect("home")
        else:
            messages.info(request, "Username or password is incorrect")
            # return render(request, "login.html")
    context = {"form": form}
    return render(request, "login.html", context)


def logoutView(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect("login")


@login_required(login_url="login")
# @allowed_users(allowed_roles=["premium", "free"])
def homeView(request):

    return render(request, "home.html")


@login_required(login_url="login")
@allowed_users(allowed_roles=["Premium"])
def postView(request):
    user = request.user
    form = postForm()
    form.user = user
    if request.method == "POST":
        form = postForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            desc = form.cleaned_data["desc"]
            cond = form.cleaned_data["cond"]
            price = form.cleaned_data["price"]
            form.save()
            post = postModel.objects.get(name=name, desc=desc, cond=cond, price=price)
            user.user_posts.add(post)
            user.save()

            messages.success(request, "Your item has been posted.")
            return redirect("home")

    return render(request, "post_item.html", {"form": form})


@login_required(login_url="login")
def buyView(request):
    items = postModel.objects.all()

    if request.method == "POST":
        form = buyForm(request.POST)
        return render(request, "buy.html", {"form": form, "items": items})

    form = buyForm()
    return render(request, "buy.html", {"form": form, "items": items})


@login_required(login_url="login")
def purchaseView(request, pk):
    item = postModel.objects.get(id=pk)
    return render(request, "purchase.html", {"item": item})


@login_required(login_url="login")
def successful_purchaseView(request, pk):
    item = postModel.objects.get(id=pk)
    item.delete()
    messages.success(request, "Item purchased!")
    return redirect("home")


@login_required(login_url="login")
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


@login_required(login_url="login")
def deleteView(request, pk):
    item = postModel.objects.get(id=pk)
    return render(request, "delete.html", {"item": item})


@login_required(login_url="login")
def successful_deleteView(request, pk):
    item = postModel.objects.get(id=pk)
    item.delete()
    messages.success(request, "Item has been deleted.")
    return redirect("home")


@login_required(login_url="login")
@allowed_users(allowed_roles=["Premium"])
def all_postsView(request):
    user = request.user
    users_posts = user.user_posts.all()
    post_list = list(users_posts)
    return render(request, "allposts.html", {"post_list": post_list})
