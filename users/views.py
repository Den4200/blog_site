from django.shortcuts import redirect, render
from django.views import View

from users.forms import LoginForm, RegisterForm

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
            messages.error(request, 'Invalid form')
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
            return redirect(redirect_url or '/')

        messages.error(request, 'Invalid username or password')
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
            messages.error(request, 'Invalid form')
            error = True

        if form.cleaned_data['password1'] != form.cleaned_data['password2']:
            messages.error(request, 'Passwords do not match')
            error = True

        if len(User.objects.filter(username=form.cleaned_data['username'])) > 0:
            messages.error(request, 'Username already exists')
            error = True

        if len(User.objects.filter(email=form.cleaned_data['email'])) > 0:
            messages.error(request, 'Email already in use')
            error = True

        if error:
            return redirect('register')

        user = User(
            email=form.cleaned_data['email'],
            username=form.cleaned_data['username']
        )
        user.set_password(form.cleaned_data['password1'])
        user.save()

        return redirect('login')
