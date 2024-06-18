"""
URL configuration for FILE_SERVER project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from django.contrib.auth import views as auth_views


from accounts import views as accounts_views
from file_server_system import views


urlpatterns = [
    path('', views.home, name = 'home'),
    path('index/', views.index, name='index'),

    # acounts urls
    path('signup/', accounts_views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    # path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('logout', accounts_views.logout_view, name='logout'),
    path('activate/<uidb64>/<token>',accounts_views.activate, name="activate"),

    # upload and download urls
    path('upload/', views.upload_document, name='upload_document'),
    path('send_email/<int:document_id>/', views.send_email, name='send_email'),
    # path('email/<int:document_id>/', views.email_document, name='email_document'),
    path('download/<int:document_id>/', views.download_document, name='download_document'),
    path('search/', views.search_documents, name='search_documents'), 
    path('admin/', admin.site.urls),

    # rest password urls
    path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
   
    path('settings/password/', auth_views.PasswordChangeView.as_view(template_name='accounts/password_change.html'), name='password_change'),
    path('settings/password/done/', auth_views.PasswordChangeDoneView.as_view(template_name='accounts/password_change_done.html'), name='password_change_done'),

]
