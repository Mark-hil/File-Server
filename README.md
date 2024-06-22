**Project Overview**
This runs a business that distributes documents such as wedding cards, admission forms, etc., 
on behalf of various businesses to different users. To scale our business, desires a digital platform 
where these documents can be easily accessed and downloaded remotely.
This project is a web application designed to fulfill that need.

**Features**

**User Features,**

1. Signup & Login,

Users can sign up and log in with an email and password.

Account verification through email.

Password reset feature to recover lost passwords.

2. **Feed Page**

Users can see a list of available files that can be downloaded.

3. **Search**

Users can search the file server for specific documents.

4. **Email Documents**

Users can send a file to an email address through the platform.

 **Admin Features**

1. **Upload Files**

Admins can upload files with a title and description.

2. **View Metrics**

Admins can see the number of downloads and the number of emails sent for each file.

**Installation**

1. Clone the repository

2. **Create a virtual environment**
use the code below to create a virtual environment 

python -m venv venv

source venv/bin/activate   # On Windows use `venv\Scripts\activate`

3. **Install dependencies**

pip install -r requirements.txt

4. **Set up the database**

python manage.py makemigrations

python manage.py migrate

5. **Create a superuser**

python manage.py createsuperuser

6. **Run the development server**

python manage.py runserver

7. **Access the application**

Open your web browser and go to http://127.0.0.1:8000.

**Configuration**

1. Email Backend Configuration

In info.py, configure the email backend to use your email service for account verification and document emailing.

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'your-email-host'

EMAIL_PORT = 587

EMAIL_USE_TLS = True

EMAIL_HOST_USER = 'your-email@example.com'

EMAIL_HOST_PASSWORD = 'your-email-password'

2. Static Files
Make sure your static files are collected and served correctly.

python manage.py collectstatic

**Usage**
1. Signup & Login

Navigate to /signup to create a new account.

Navigate to /login to log into your account.

Verify your email after signup to activate your account.

2. Feed Page

After logging in, navigate to the home page to see the list of available documents.

3. Search

Use the search bar on the home page to find specific documents.

4. Email Documents

On the document list, click on "Send Email" to email the document to a specified address.

5. Admin Actions

Log in as an admin and navigate to the admin panel to upload new documents and view metrics.
