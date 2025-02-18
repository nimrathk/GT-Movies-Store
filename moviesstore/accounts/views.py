from django.contrib.auth.tokens import default_token_generator
from django.shortcuts import render

# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from .forms import CustomUserCreationForm, CustomErrorList
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required
def logout(request):
    auth_logout(request)
    return redirect('home.index')

def login(request):
    template_data = {}
    template_data['title'] = 'Login'
    if request.method == 'GET':
        return render(request, 'accounts/login.html',
            {'template_data': template_data})
    elif request.method == 'POST':
        user = authenticate(
            request,
            username = request.POST['username'],
            password = request.POST['password']
        )
        if user is None:
            template_data['error'] = 'The username or password is incorrect.'
            return render(request, 'accounts/login.html',
                {'template_data': template_data})
        else:
            auth_login(request, user)
            return redirect('home.index')

def signup(request):
    template_data = {}
    template_data['title'] = 'Sign Up'
    if request.method == 'GET':
        template_data['form'] = CustomUserCreationForm()
        return render(request, 'accounts/signup.html',
            {'template_data': template_data})
    elif request.method == 'POST':
        form = CustomUserCreationForm(request.POST, error_class=CustomErrorList)
        if form.is_valid():
            form.save()
            return redirect('accounts.login')
        else:
            template_data['form'] = form
            return render(request, 'accounts/signup.html', {'template_data': template_data})

@login_required
def orders(request):
    template_data = {}
    template_data['title'] = 'Orders'
    template_data['orders'] = request.user.order_set.all()
    return render(request, 'accounts/orders.html',
        {'template_data': template_data})

def request_reset(request):
    template_data = {'title': 'Reset Password'}
    if request.method == 'GET':
        return render(request, 'accounts/request_reset.html',
                      {'template_data': template_data})
    elif request.method == 'POST':
        username = request.POST.get('username')
        answer1 = request.POST['security1']
        answer2 = request.POST['security2']
    try:
        user = User.objects.get(username=username)
        correct_answers = SecurityQuestions.objects.get(user=user)
        if check_password(answer1, correct_answers.answer1) and check_password(answer2, correct_answers.answer2):
            token = default_token_generator.make_token(user)
            return redirect('accounts:password_reset', username=username, token=token)
        else:
            template_data['error'] = 'At least one of the answers is incorrect.'
            return render(request, 'accounts/request_reset.html',{'template_data': template_data})
    except User.DoesNotExist:
        template_data['error'] = 'This user does not exist.'
        return render(request, 'accounts/request_reset.html', {'template_data': template_data})

def password_reset(request, username, token):
    template_data = {'title': 'Set New Password'}
    try:
        user = get_user_model().objects.get(username=username)
        if default_token_generator.check_token(user, token):
            if request.method == 'POST':
                form = SetPasswordForm(user, request.POST)
                if form.is_valid():
                    form.save()
                    return redirect('accounts:login')
            else:
                form = SetPasswordForm(user)
            return render(request, 'accounts/password_reset.html', {'template_data': template_data, 'form': form})
        else:
            template_data['error'] = 'Invalid reset token.'
            return render(request, 'accounts/password_reset.html', {'template_data': template_data})
    except User.DoesNotExist:
        template_data['error'] = 'Invalid user.'
        return render(request, 'accounts/password_reset.html', {'template_data': template_data})