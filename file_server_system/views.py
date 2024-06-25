from email.message import EmailMessage
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import Document
from .forms import DocumentForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import EmailMessage
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    query = request.GET.get('search')
    if query:
        documents = Document.objects.filter(title__icontains=query)
    else:
        documents = Document.objects.all()

    paginator = Paginator(documents, 10)  # Show 10 documents per page
    page = request.GET.get('page')
    try:
        documents = paginator.page(page)
    except PageNotAnInteger:
        documents = paginator.page(1)
    except EmptyPage:
        documents = paginator.page(paginator.num_pages)

    return render(request, 'home.html', {'documents': documents, 'page_obj': documents})

def search_documents(request):
    query = request.GET.get('query', '')
    if query:
        documents = Document.objects.filter(title__icontains=query)
    else:
        documents = Document.objects.all()
    
    document_list = list(documents.values('id', 'title', 'description', 'download_count', 'email_count'))
    return JsonResponse({'documents': document_list})

def index(request):
    documents = Document.objects.all()
    return render(request, 'home.html', {'documents': documents})

@login_required
def upload_document(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'upload_document.html', {'form': form})

@login_required
def download_document(request, document_id):
    document = get_object_or_404(Document, pk=document_id)
    document.download_count += 1
    document.save()
    response = HttpResponse(document.file, content_type='application/octet-stream')
    response['Content-Disposition'] = f'attachment; filename="{document.file.name}"'
    return response

# def send_email(request, document_id):
#     document = get_object_or_404(Document, pk=document_id)

#     if request.method == 'POST':
#         recipient_email = request.POST.get('recipient_email')

#         email = EmailMessage(
#             subject='Here is your document',  # Subject
#             body='Attached is the document you requested.',  # Body
#             from_email='chillop.learn@gmail.com',  # From email
#             to=[recipient_email],  # To email
#         )
#         email.attach_file(document.file.path)
#         try:
#             email.send()
#             messages.success(request, "Email sent successfully!")
#         except Exception as e:
#             messages.error(request, f"An error occurred: {e}")

#         document.email_count += 1
#         document.save()

#         return redirect('home')

#     return render(request, 'send_email.html', {'document': document})
@login_required
def send_email(request, document_id):
    document = get_object_or_404(Document, pk=document_id)

    if request.method == 'POST':
        recipient_emails = request.POST.get('recipient_emails')
        email_list = [email.strip() for email in recipient_emails.split(',') if email.strip()]

        if email_list:
            email = EmailMessage(
                'Here is your document',  # Subject
                'Attached is the document you requested.',  # Body
                'chillop.learn@gmail.com',  # From email
                email_list,  # To email list
            )
            email.attach_file(document.file.path)
            email.send()

            document.email_count += len(email_list)
            document.save()

            return redirect('home')

    return render(request, 'send_email.html', {'document': document})
    