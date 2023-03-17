"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path("", views.homeView, name="home"),
    path("post/", views.postView, name="post"),
    path("signup/", views.signupView, name="signup"),
    path("login/", views.loginView, name="login"),
    path("buy/", views.buyView, name="buy"),
    path("purchase/<pk>/", views.purchaseView, name="purchase"),
    path(
        "successful_purchase/<pk>/",
        views.successful_purchaseView,
        name="successful_purchase",
    ),
    path("update/<pk>/", views.updateView, name="update"),
    path("delete/<pk>/", views.deleteView, name="delete"),
    path(
        "successful_delete/<pk>/", views.successful_deleteView, name="successful_delete"
    ),
    path("allusers/", views.allusersView, name="allusers"),
    path("admin/", admin.site.urls),
]
