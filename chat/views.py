from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm, NotesForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Notes, User

# Create your views here.

#AUTHENTICATION

def index(request):
    title="Home Page"
    return render(request, 'index.html',{"title": title})

def register(request):
    title="RegistrationPage"
    message=None
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            message = "You have successfully registered"
            return redirect('login')
        else:
            message = "Form is not valid"

    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html',{'form': form, 'message': message, 'title': title})

def login_view(request):
    title="LoginPage"
    form = LoginForm(request.POST or None)
    message=None

    if request.method == 'POST' :
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None and user.is_admin:
                login(request, user)
                return redirect('adminpage')
                
            elif user is not None and user.is_customer:
                login(request, user)
                return redirect('customerPage')

            else:
                message = 'Invalid Credentials'
        else:
            message = 'Error validating Form'
    return render( request, 'accounts/login.html', {'form': form, 'message': message, 'title': title})

def logoutUser(request):
    logout(request)
    return redirect('home')

@login_required(login_url='/')
def adminpage(request):
    notes = Notes.objects.all()
    return render( request, 'admin.html', {'notes': notes})

@login_required(login_url='/')
def customer(request):
    args= request.user.pk
    notes = Notes.objects.filter(author=args)
    return render( request, 'customer.html', {'notes': notes})


#NOTES

def new_note(request):
    if request.method == 'POST':
        form = NotesForm(request.POST)
        if form.is_valid():
            forms = form.save(commit=False)
            forms.author = request.user
            forms.save()
            if request.user.is_admin:
                return redirect('adminpage')
            if request.user.is_customer:
                return redirect('customerPage')

    else:
        form = NotesForm()
    return render( request, "new_note.html", {"form": form})

def note_detail(request, pk):
    message=None
    note = Notes.objects.get(id=pk)
    form = NotesForm(instance=note)
    if request.method == 'POST':
        form = NotesForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            message = 'Note has been added'
            if request.user.is_admin:
                return redirect('adminpage')
            if request.user.is_customer:
                return redirect('customerPage')

    return render( request, "note_detail.html", {'note': note, 'form':form, 'message': message })

def delete_note(request, pk):
    message=None
    note = Notes.objects.get(id=pk)
    form = NotesForm(instance=note)
    if request.method == 'POST':
        note.delete()
        message = 'Your note has been deleted'
        if request.user.is_admin:
            return redirect('adminpage')
        if request.user.is_customer:
            return redirect('customerPage')

    return render( request, "delete.html", {"note":note, "form":form, "messages":message})
