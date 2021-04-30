from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import logout, authenticate, login as auth_login
from main.forms import *
from main.models import *


def homepage(request):
    return render(request=request,
                  template_name='main/home.html')


def login(request):
    if request.method == 'POST':
        form = LoginForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                messages.success(request, 'Logged In ')
                return redirect('/')
            else:
                messages.add_message(request, messages.INFO, 'Invalid username or password.')
        else:
            messages.add_message(request, messages.INFO, 'Invalid username or password.')
    form = LoginForm()
    return render(request=request,
                  template_name="main/login.html",
                  context={"form": form})


def contact(request):
    return render(request=request,
                  template_name='main/contact.html')


def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("main:homepage")


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            email = form.cleaned_data.get('email')
            fn = form.cleaned_data.get('first_name')
            ln = form.cleaned_data.get('last_name')
            mob = form.cleaned_data.get('mobile')
            city = form.cleaned_data.get('city')
            messages.success(request, 'Your account created successfully!')
            auth_login(request, user)
            p = Register(username=username, first_name=fn, last_name=ln, email=email, mobile=mob, city=city)
            p.save()
            return redirect("main:homepage")

        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")

    form = SignUpForm
    return render(request=request,
                  template_name="main/register.html",
                  context={"form": form})


def profile(request, username):
    just = Register.objects.filter(username=username).last()
    if just is not None:
        pro = just.profile
    else:
        pro = None
    form = RegForm(instance=just)

    if request.method == 'POST':
        form = RegForm(request.POST, instance=just)
        if form.is_valid():
            form.save()
            just = Register.objects.filter(username=username).last()
            just.profile = pro
            just.save()
        return redirect('main:academicProfile', username=username)
    else:
        return render(request, 'main/comm_profile.html', {'form': form})


def academicProfile(request, username):
    reg = Register.objects.filter(username=username).last()
    if reg.profile is not None:
        pro = reg.profile.alumni_data
    else:
        pro = None
    form = BioForm(instance=reg.profile)

    if request.method == 'POST':
        form = BioForm(request.POST, instance=reg.profile)
        if form.is_valid():
            form.save()
            if reg.profile is None:
                ins = ProfileForm.objects.all().last()
                reg.profile = ins
                reg.save()
            reg = Register.objects.filter(username=username).last()
            print(reg.profile, reg.profile.alumni_data, pro)
            r = reg.profile
            r.alumni_data = pro
            r.save()
        return redirect('main:job_details', username=username)
    else:
        return render(request, 'main/profile.html', {'form': form})


def job_details(request, username):
    reg = Register.objects.filter(username=username).last()
    alu = reg.profile.alumni_data
    # just = ProfileForm.objects.all().last()
    if reg.profile.role != "ALU":
        return redirect('main:homepage')
    form = AluForm(instance=alu)

    if request.method == 'POST':
        form = AluForm(request.POST, instance=alu)
        if form.is_valid():
            form.save()
            ins = AlumniForm.objects.all().last()
            r = reg.profile
            r.alumni_data = ins
            r.save()
        return redirect('main:homepage')
    else:
        return render(request, 'main/job_detail.html', {'form': form})
