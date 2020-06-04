from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.shortcuts import redirect, render
from django.views import View

from users.forms import LoginForm, RegisterForm
from users.models import User


class ProfileView(LoginRequiredMixin, View):
    template_name = 'users/profile.html'

    def get(self, request, user_id=None):
        if user_id is None:
            return redirect('profile', user_id=request.user.id)

        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            raise Http404('User does not exist')
        else:
            # TODO: Compare user query with request user to see if the profile can be edited
            return render(request, self.template_name, {'user_query': user})


class LoginView(View):
    template_name = 'users/login.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/')

        form = LoginForm()
        request.session['next'] = request.GET.get('next')
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        if request.user.is_authenticated:
            return redirect('/')

        form = LoginForm(request.POST)

        if not form.is_valid():
            messages.error(request, 'Invalid form', extra_tags='danger')
            return redirect('login')

        user = authenticate(
            request,
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password']
        )

        if user is not None:
            login(request, user)

            redirect_url = request.session.get('next')
            request.session['next'] = None

            messages.success(request, 'Login successful')

            return redirect(redirect_url or '/')

        messages.error(request, 'Invalid username or password', extra_tags='danger')
        return redirect('login')


class RegisterView(View):
    template_name = 'users/register.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/')

        form = RegisterForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        if request.user.is_authenticated:
            return redirect('/')

        form = RegisterForm(request.POST)

        error = False

        if not form.is_valid():
            messages.error(request, 'Invalid form', extra_tags='danger')
            error = True

        else:
            if form.cleaned_data['password1'] != form.cleaned_data['password2']:
                messages.error(request, 'Passwords do not match', extra_tags='danger')
                error = True

            if len(User.objects.filter(username=form.cleaned_data['username'])) > 0:
                messages.error(request, 'Username already exists', extra_tags='danger')
                error = True

            if len(User.objects.filter(email=form.cleaned_data['email'])) > 0:
                messages.error(request, 'Email already in use', extra_tags='danger')
                error = True

        if error:
            return redirect('register')

        user = User(
            email=form.cleaned_data['email'],
            username=form.cleaned_data['username']
        )
        user.set_password(form.cleaned_data['password1'])
        user.save()

        messages.success(request, 'Registration successful')

        return redirect('login')
