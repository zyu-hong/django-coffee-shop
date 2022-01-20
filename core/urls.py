"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from utils.auth_views import register
from django.urls import path, include, reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetConfirmView

password_set_params = {
    'template_name': 'users/password_set.html',
    'post_reset_login': True,
    'success_url': reverse_lazy('login'),
}
password_reset_params = {
    'template_name': 'users/password_reset.html',
    'email_template_name': 'users/password_reset/email.html',
    'subject_template_name': 'users/password_reset/subject.txt',
    'success_url': reverse_lazy('login'),
}
login_params = {
    'template_name': 'users/login.html',
    'redirect_authenticated_user': True,
}
urlpatterns = [
    path('', lambda request: redirect('coffees:index'), name='root'),
    path('coffees/', include('coffees.urls')),
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(**login_params), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
    path(
        'password-reset/',
        PasswordResetView.as_view(**password_reset_params),
        name='password_reset',
    ),
    path(
            'password-set/<uidb64>/<token>/',
            PasswordResetConfirmView.as_view(**password_set_params),
            name='password_set',
        ),
]
handler403 = 'utils.error_handlers.permission_denied'
handler404 = 'utils.error_handlers.page_not_found'
