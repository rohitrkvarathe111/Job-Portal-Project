from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from django.contrib import messages

from .models import User
from .form import RegisterUserForm
from resume.models import Resume
from company.models import Company

# Create your views here.
def register_applicant(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.is_applicant = True
            var.username = var.email
            var.save()

            Resume.objects.create(user=var)
            messages.info(request, 'Your account has been created, pls log in here')
            return redirect('login')
        else:
            messages.warning(request, 'Something went worng')
            return redirect('register-applicant')
    else:
        form = RegisterUserForm()
        context = {'form':form}
        return render(request, 'users/register_applicant.html', context)


# register job poster
def register_recruiter(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.is_recruiter = True
            var.username = var.email
            var.save()

            Company.objects.create(user=var)
            messages.info(request, 'Your account has been created , please log in here')
            return redirect('login')
        else:
            messages.warning(request, 'Something went worng')
            return redirect('register-recruiter')
    else:
        form = RegisterUserForm()
        context = {'form':form}
        return render(request, 'users/register_recruiter.html', context)

  
# user log in
def login_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)

        if user is not None and user.is_active:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.warning(request, 'Sonthing went worng')
            return redirect('login')
        
    else:
        return render(request, 'users/login.html')
    

# user logout
def logout_user(request):
    logout(request)
    messages.info(request, 'your session has ended')
    return redirect('login')




#===================================================================


def all_users(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'users/all_user.html', context)










#==================================================================================

from django.contrib.auth.decorators import user_passes_test



def is_admin(user):
    return user.is_authenticated and user.is_staff

@user_passes_test(is_admin)
def admin_view(request):
    applicants = User.objects.filter(is_applicant=True)
    recruiters = User.objects.filter(is_recruiter=True)

    context = {
        'applicants': applicants,
        'recruiters': recruiters,
    }

    return render(request, 'users/admin_view.html', context)

@user_passes_test(is_admin)
def delete_user(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        user.delete()
        messages.success(request, 'User deleted successfully.')
    except User.DoesNotExist:
        messages.warning(request, 'User not found.')
    
    return redirect('admin-view')


