from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import *
from .forms import NoteModelForm, CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required


# Create your views here.

# login, register, menu

def register_view(req):
    form = CreateUserForm()

    if req.method == "POST":
        form = CreateUserForm(req.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(req, 'account has been created for ' + user)
            return redirect('yunote:login')

    con = {'form': form}
    return render(req, 'register.html', con)


def login_view(req):
    if req.method == 'POST':
        username = req.POST.get('username')
        password = req.POST.get('password')

        user = authenticate(req, username=username, password=password)

        if user is not None:
            login(req, user)
            return redirect('yunote:home')
        else:
            messages.info(req, 'username or password is incorrect')
            return render(req, 'login.html',)

    con = {}
    return render(req, 'login.html', con)


def logout_view(req):
    logout(req)
    return redirect('yunote:user')


def logoutUser(req):
    return render(req, 'logout.html')


# CRUD create, delete, retrieve, update

def home_view(req):
    con = {}
    return render(req, 'home.html', con)

@login_required(login_url='yunote:login')
def create_view(req):
    form = NoteModelForm(req.POST or None, req.FILES or None)
    if form.is_valid():
        form.instance.user = req.user
        form.save()
        return redirect('yunote:list_view')

    context = {
        'form': form
    }

    return render(req, "create.html", context)


def list_view(request):
    notes = Note.objects.all()
    context = {
        'object_list': notes
    }
    return render(request, "list.html", context)


def delete_view(req, id):
    item_to_delete = Note.objects.filter(pk=id)
    if item_to_delete.exists():
        if req.user == item_to_delete[0].user:
            item_to_delete[0].delete()
    return redirect('yunote:list_view')


def update_view(request, id):
    unique_note = get_object_or_404(Note, id=id)
    form = NoteModelForm(request.POST or None, request.FILES or None, instance=unique_note)
    if form.is_valid():
        form.instance.user = request.user
        form.save()
        return redirect('yunote:list_view')

    context = {
        'form': form
    }

    return render(request, "create.html", context)
