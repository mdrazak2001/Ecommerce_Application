from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Profile
import uuid
from django.conf import settings
from django.core.mail import send_mail
import os
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import *
from django.http import HttpResponseRedirect
import time
from .mail import *
# Create your views here.


def home(request):
    context = {}
    products = Product.objects.all()
    context['products'] = products
    return render(request, 'base/home.html', context)


def userLogout(request):
    logout(request)
    return redirect('home')


def userLogin(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user_ob = User.objects.filter(username=username).first()
        if user_ob is None:
            messages.add_message(request, messages.INFO, 'User not found')
            return redirect('login')

        profile_ob = Profile.objects.filter(user=user_ob).first()

        if profile_ob.is_verified == False:
            messages.add_message(request, messages.INFO,
                                 'Your profile isnt verified check your mail')
            return redirect('login')

        user = authenticate(username=username, password=password)
        if user is None:
            messages.add_message(request, messages.INFO,
                                 'Wrong creds')
            return redirect('login')
        login(request, user)
        return redirect('home')
    page = 'login'
    return render(request, 'base/login_register.html', {'page': page})


def userRegister(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        try:
            if User.objects.filter(email=email).first() is not None:
                print(User.objects.filter(email=email).first())
                messages.add_message(
                    request, messages.INFO, 'email name taken')
                render(request, 'base/login_register.html')

            elif User.objects.filter(username=username).first() is not None:
                messages.add_message(request, messages.INFO, 'User name taken')
                render(request, 'base/login_register.html')

            else:
                user_ob = User.objects.create(username=username, email=email)
                user_ob.set_password(password)
                user_ob.save()
                auth_token = str(uuid.uuid4())

            profile_ob = Profile.objects.create(
                user=user_ob, auth_token=auth_token)
            profile_ob.save()

            send_mail_after_registration(email, auth_token)
            return redirect('token_send')

        except Exception as e:
            print(e)
    page = 'register'
    return render(request, 'base/login_register.html', {'page': page})


def token_send(request):
    return render(request, 'base/token.html')


def verify(request, auth_token):
    try:
        profile_obj = Profile.objects.filter(auth_token=auth_token).first()
        if profile_obj:
            if(profile_obj.is_verified):
                messages.add_message(
                    request, messages.INFO, 'Your Account is already verified now you can login!!')
                return redirect('login')

            profile_obj.is_verified = True
            profile_obj.save()
            messages.add_message(
                request, messages.INFO, 'Your Account is verified now you can login!!')
            return redirect('login')
        else:
            messages.add_message(
                request, messages.INFO, 'error occured')
    except Exception as e:
        print(e)


@login_required(login_url='login')
def addProduct(request):
    form = ProductForm()
    if request.method == 'POST':
        price = request.POST.get('price_in_rupees')
        product_name = request.POST.get('product_name')
        descripton = request.POST.get('descripton')
        Images = request.FILES.getlist('images')
        # print(Images)
        user = request.user
        try:
            profile = Profile.objects.filter(user=user).first()
            product_ob = Product.objects.create(created_by=profile, price_in_rupees=price,
                                                product_name=product_name, descripton=descripton)
            print(user)
            product_ob.save()
            for image in Images:
                pimg = ProductImage.objects.create(
                    images=image, product=product_ob)
                pimg.save()
        except Exception as e:
            print(e)

    return render(request, 'base/add_product.html', {'form': form})


def forgotPassword(request):
    page = 'forgot'
    if request.user.is_authenticated:
        return redirect('home')
    try:
        if request.method == 'POST':
            username = request.POST.get('username')
            if not User.objects.filter(username=username).first():
                messages.add_message(
                    request, messages.INFO, 'no such accout')
                return redirect('forgot-password')

            user_obj = User.objects.filter(username=username).first()
            email = user_obj.email
            profile_obj = Profile.objects.filter(user=user_obj).first()
            auth_token = profile_obj.auth_token
            send_mail_after_forgot(email, auth_token)
            messages.add_message(
                request, messages.INFO, 'Check Mail for reset link')

    except Exception as e:
        print(e)

    return render(request, 'base/login_register.html', {'page': page})


def changePassword(request, auth_token):
    if request.user.is_authenticated:
        return redirect('home')
    token = auth_token
    if request.method == 'POST':
        try:
            profile_obj = Profile.objects.filter(auth_token=token).first()
            if profile_obj is not None:
                p1 = request.POST['p1']
                p2 = request.POST['p2']
                if p1 != p2:
                    messages.add_message(
                        request, messages.INFO, 'Passwords dont match Re enter')
                    return redirect(f'/changepassword/{token}')
                user = profile_obj.user
                uo = User.objects.filter(username=user).first()
                uo.set_password(p1)
                uo.save()
                messages.add_message(
                    request, messages.INFO, 'Password Reset Try Logging in now!')
                time.sleep(3)
                return redirect('login')
            else:
                messages.add_message(
                    request, messages.INFO, 'error occured')
        except Exception as e:
            print(e)

    return render(request, 'base/changepassword.html')
