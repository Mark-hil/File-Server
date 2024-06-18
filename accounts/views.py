from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from .tokens import generate_token
from django.core.mail import EmailMessage
from FILE_SERVER import settings
from .forms import SignUpForm
from django.contrib.auth import logout
# from email.message import EmailMessage

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            # Send welcome email
            subject = "Welcome to File Server"
            message = f"Hello {user.first_name}!! \nWelcome to File Server!! \nThank you for visiting our website. \nWe have also sent you a confirmation email, please confirm your email address in order to activate your account.\n\nThank You\nMark"
            from_email = settings.EMAIL_HOST_USER
            to_list = [user.email]
            send_mail(subject, message, from_email, to_list, fail_silently=True)

            # Email Address Confirmation Email
            current_site = get_current_site(request)
            email_subject = "Confirm your email @ File Server!!"
            message2 = render_to_string('email_confirmation.html', {
                'name': user.first_name,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': generate_token.make_token(user),
            })

            email = EmailMessage(
                email_subject,
                message2,
                settings.EMAIL_HOST_USER,
                [user.email],
            )
            email.fail_silently = True
            email.send()

            messages.success(request, "Your account has been successfully created. We have also sent you a confirmation email, please confirm your email address to activate your account.")
            return redirect('home')
        else:
            messages.error(request, "There was an error with your form. Please correct the errors and try again.")
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!")
    return redirect('login')


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        myuser = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        myuser = None

    if myuser is not None and generate_token.check_token(myuser, token):
        myuser.is_active = True
        myuser.save()
        login(request, myuser)
        messages.success(request, "Your Account has been activated!!")
        return redirect('login')  
    else:
        return render(request, 'activation_failed.html')


