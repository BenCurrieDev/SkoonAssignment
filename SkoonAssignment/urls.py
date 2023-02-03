from django.contrib import admin
from django.urls import path

from UCalculator import views
from accounts import views as accounts_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('skoon-admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signup/', accounts_views.signup, name="signup"),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('database', views.database, name="database"),
]
