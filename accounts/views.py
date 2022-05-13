from blog.models import Comment
from django.shortcuts import redirect, render
from django.contrib import messages, auth
from django.contrib.auth.models import User
# Create your views here.


def register(request):
    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username is already exists')
                return redirect('register')
            else:
                if User.objects.filter(email=email):
                    messages.error(request, 'Email is already exists')
                    return redirect('register')
                else:
                    user = User.objects.create_user(first_name=firstname,
                                                    last_name=lastname,
                                                    username=username,
                                                    email=email,
                                                    password=password)
                    user.save()
                    auth.login(request, user)
                    messages.success(request,
                                     'Your Registration is Succesfull')
                    return redirect('profile')

        else:
            messages.error(request, 'your passwords are not the same')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')

 
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password) 
        if user is not None:
             auth.login(request, user)
             messages.success(request, 'you are successfully login')
             return redirect('profile')
        else:
             messages.error(request, 'username or password is not correct')
             return redirect('login')

    return render(request, 'accounts/login.html')


def logout(request):
    auth.logout(request)
    messages.success(request, 'You are successfuly logout')
    return redirect('login')


def profile(request):
    if request.user.is_authenticated:
         return render(request, 'accounts/profile.html')
    else:
         messages.info(request, 'you must first login to see this page')
         return redirect('login')
    


def myComments(request):
    if request.user.is_authenticated:
         comments = Comment.objects.filter(user_name=request.user.username)
         return render(request, 'accounts/mycomments.html', {
              'comments': comments,
         })
    else:
         messages.info(request, 'you must first login to see this page')
         return redirect('login')
