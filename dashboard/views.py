from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard:home')  # Update this as per your URL name
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'dashboard/login.html', {'form': form})
@login_required(login_url='dashboard:login')  
def home(request):
    return render(request, 'dashboard/home.html')


def logout_view(request):
    logout(request)
    return redirect('dashboard:login')  # Redirect to login or home