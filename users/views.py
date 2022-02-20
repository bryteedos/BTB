from django.shortcuts import redirect, render
from django.contrib import messages
from.forms import registerform
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm 

# Create your views here.
@login_required
def usersprofile(request):
    return render (request, 'users/profile.html')

def register(request):
    if request.method == 'POST':
        form=registerform(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request, f'Welcome {username}, Your Account Is Created Successfully')
            return redirect ('login')
    else:
        form=registerform()
    return render(request, 'users/register.html', {'form':form})