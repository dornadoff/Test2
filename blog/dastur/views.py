from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from django.views import View
from .models import *

class LoginView(View):
    def post(self, request):
        user = authenticate(username=request.POST.get("username"),
                            password=request.POST.get("password"))
        if user is None:
            return redirect("/")
        else:
            login(request, user)
            return redirect("/blog/")

    def get(self, request):
        return render(request, "login.html")


class RegisterView(View):
    def post(self, request):
        if request.POST.get("username") != User.objects.filter(username="username") and request.POST.get("password") == request.POST.get("password"):
            user1 = User.objects.create_user(username=request.POST.get("username"),
                                            password = request.POST.get("password"))
            Muallif.objects.create(
                ism = request.POST.get("ism"),
                yosh = request.POST.get("yosh"),
                kasb = request.POST.get("kasb"),
                user = user1
            )
            return redirect("/")

    def get(self, request):
        return render(request, "register.html")


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("/")

class BlogView(View):
    def get(self, request):
        if request.user.is_authenticated:
            muallif1 = Muallif.objects.get(user=request.user)
            data = {
                "blog":Maqola.objects.filter(muallif=muallif1),
                "muallif":Muallif.objects.all()
            }
            return render(request, "blog.html", data)

    def post(self, request):
        Maqola.objects.create(
            sarlavha=request.POST.get("sarlavha"),
            sana = request.POST.get("sana"),
            mavzu=request.POST.get("mavzu"),
            matn = request.POST.get("matn"),
            muallif = Muallif.objects.get(id=request.POST.get("muallif"))
        )
        return redirect("/blog/")

class MaqolaView(View):
    def get(self, request, pk):
        if request.user.is_authenticated:
            user1 = Muallif.objects.filter(user=request.user)
            data = {"maqola":Maqola.objects.get(id=pk, muallif=user1)}
            return render(request, "maqola.html", data)




