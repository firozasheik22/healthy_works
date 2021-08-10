from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm,PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
# Create your views here.
@login_required
def profile(request):
    if request.method == 'POST':
        
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request,'Successfully updated')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        

    context = {
        'u_form': u_form,
    }
    

    return render(request, 'profile.html',context)

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'profile.html', {
        'form': form
    })
