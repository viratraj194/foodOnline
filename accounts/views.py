from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from vendor.forms import VendorForms
from . forms import UserForm
from . models import User, UserProfile
from django.contrib import messages, auth
from .utlis import detectUser, send_verification_email
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.exceptions import PermissionDenied
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from .models import *
from django.template.defaultfilters import slugify
from vendor.models import Vendor
from orders.models import Order
import datetime

def registerUser(request):
    if request.user.is_authenticated:
        messages.warning(request, 'you are already logged in')
        return redirect('myAccount')
    elif request.method == 'POST':
        #print(request.POST)
        
        form = UserForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            user = form.save(commit=False)
            user.set_password(password)
            user.role = User.CUSTOMER
            user.save()
            #send email verification
            mail_subject = 'please activate your account'.title()
            mail_template = 'accounts/emails/account_verification_email.html'
            send_verification_email(request, user, mail_subject, mail_template)
            messages.success(request, 'your account has been registered successfully! please wait for approval')
            return redirect('home')
        else:
            print('form is invalid ')
            print(form.errors)
    else:
        form = UserForm
    context = {
        'form': form
    }
    return render(request, 'accounts/registerUser.html', context)

def registerVendor(request):
    if request.user.is_authenticated:
        messages.warning(request, 'you are already logged in')
        return redirect('myAccount')
    elif request.method == 'POST':
        form = UserForm(request.POST)
        v_form = VendorForms(request.POST, request.FILES)
        if form.is_valid() and v_form.is_valid():
            first_name = form.cleaned_data['last_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
            user.role = User.VENDOR
            user.save()
            vendor = v_form.save(commit=False)
            vendor.user = user
            vendor_name = v_form.cleaned_data['vendor_name']
            vendor.vendor_slug = slugify(vendor_name)+'-'+str(user.id)
            user_profile = UserProfile.objects.get(user = user)
            vendor.user_profile = user_profile
            vendor.save()
            # send email verification
            mail_subject = 'please activate your account'.title()
            mail_template = 'accounts/emails/account_verification_email.html'
            send_verification_email(request, user, mail_subject, mail_template)
            messages.success(request, 'your account has been registered successfully! please wait for approval')
            return redirect('registerVendor')
        else:
            print('invalid form')
            print(form.errors)

    else:
        form = UserForm()
        v_form = VendorForms
    context = {
        'form': form,
        'v_form': v_form
    }
    return render(request, 'accounts/registerVendor.html', context)

#activate user by setting the is_active status true
def activate(request, uidb64, token):

    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, "configuration! account is activated. ")

        return redirect('myAccount')
    else:
        messages.error(request, 'invalid activation link')
        return redirect('myAccount')


def login(request):
    if request.user.is_authenticated:
        messages.warning(request, 'you are already logged in')
        return redirect('myAccount')
    elif request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(email =email, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'you logged in successfully'.title())
            return redirect('myAccount')

        else:
            messages.error(request,'invalid login credentials')
            return redirect('login')
    return render(request, 'accounts/login.html')


def logout(request):
    auth.logout(request)
    messages.info(request, 'you have logged out')
    return redirect('login')


@login_required(login_url = 'login')
def myAccount(request):
    user = request.user
    redirectUrl = detectUser(user)

    return redirect(redirectUrl)
#ristrict user from going in to the vendor dashboard
def check_role_for_vendor(user):
    if user.role == 1:
        return True
    else:
        raise PermissionDenied



#ristrict user from going in to the costumer dashboard
def check_role_for_customer(user):
    if user.role == 2:
        return True
    else:
        raise PermissionDenied

@login_required(login_url = 'login')
@user_passes_test(check_role_for_customer)
def custDashboard(request):
    orders = Order.objects.filter(user = request.user,is_ordered = True)
    recent_order = orders[:5]
    context = {
        'orders':orders,
        'orders_count':orders.count(),
        'recent_order':recent_order,
    }
    return render(request, 'accounts/custDashboard.html',context)



@login_required(login_url = 'login')
@user_passes_test(check_role_for_vendor)
def vendorDashboard(request):
    vendor = Vendor.objects.get(user = request.user)
    orders = Order.objects.filter(vendors__in = [vendor.id],is_ordered = True).order_by('-created_at')
    recent_order = orders[:5]
    #current month revenue
    current_month = datetime.datetime.now().month
    current_month_orders = orders.filter(vendors__in = [vendor.id],created_at__month = current_month)
    current_month_revenue = 0
    for i in current_month_orders:
        current_month_revenue += i.get_total_by_vendor()['grand_total']
    print(current_month_revenue)
    #total revenue
    total_revenue = 0
    for i in orders:
        total_revenue += i.get_total_by_vendor()['grand_total']
    context = {
        'orders':orders,
        'order_count':orders.count(),
        'recent_order':recent_order,
        'total_revenue':total_revenue,
        'current_month_revenue':current_month_revenue,
    }
    return render(request, 'accounts/vendorDashboard.html',context)


def forgot_password(request):
    if request.method == 'POST':
        email = request.POST['email']
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email__exact=email)
            #send reset password email
            mail_subject = 'reset your password'.title()
            mail_template = 'accounts/emails/reset_password_email.html'
            send_verification_email(request, user, mail_subject, mail_template)
            messages.success(request, 'reset password  link is sent to email  '.title())
            return redirect('login')
        else:
            messages.error(request, 'email does not exist'.title())
            return redirect('forgot_password')
    return render(request, 'accounts/forgot_password.html')

def reset_password_validate(request, uidb64, token):
    #validate user by decode
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):

        user = None

    if user is not None and default_token_generator.check_token(user, token):
        request.session['uid'] = uid
        messages.info(request, 'please reset your password')
        return redirect('reset_password')
    else:
        messages.error(request,'This link has been expired')
        return redirect('myAccount')


def reset_password(request):
    if request.method == 'POST':
        password = request.POST['password']
        conform_password = request.POST['conform_password']
        if password == conform_password:
            pk = request.session.get('uid')
            user = User.objects.get(pk=pk)
            user.set_password(password)
            user.is_active = True
            user.save()
            messages.success(request, 'password reset is successful'.title())
            return redirect('login')
        else:
            messages.error(request, 'password do not match.'.title())
            return redirect('reset_password')
    return render(request, 'accounts/reset_password.html')

#first_name = form.cleaned_data['first_name']
            # last_name = form.cleaned_data['last_name']
            #username = form.cleaned_data['username']
            #email = form.cleaned_data['email']
            #password = form.cleaned_data['password']
            #user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
            # user.role = User.CUSTOMER
            #user.save()








