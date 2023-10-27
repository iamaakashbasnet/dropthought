from django.urls import path
from django.contrib.auth import views as auth_views

from . import views as accounts_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True,
         template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', accounts_views.signup, name='signup'),
    path('settings/', accounts_views.settings, name='settings'),
    path('delete/', accounts_views.delete_account, name='delete'),
    # Ordering!!!
    path('<str:username>/', accounts_views.Profile.as_view(), name='profile'),
    path('activate/<uidb64>/<token>/',
         accounts_views.activate_account, name='activate'),
]
