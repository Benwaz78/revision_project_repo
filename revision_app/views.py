from django.shortcuts import render
from revision_app.models import About, Service
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from revision_app.forms import RegForm, AboutForm


# Create your views here.

def about_form(request):
	if request.method == 'POST':
		about_form = AboutForm(request.POST)

		if about_form.is_valid():
			about_form.save()
	else:
		about_form = AboutForm()
		return render(request, 'front_end/about_form.html', {'abt_form':about_form})


def index(request):
	show_service = Service.objects.all()

	show_about = About.objects.all()

	home_dict = {
		'serv_key':show_service,
		'abt_key':show_about
	}

	return render(request, 'front_end/index.html', context=home_dict)

def about(request):
	list_abt = About.objects.all()
	return render(request, 'front_end/about.html', {'abt_list':list_abt})

def users(request):
	list_usr = User.objects.all()
	return render(request, 'front_end/users.html', {'usr_list':list_usr})

def service(request):
	list_srv = Service.objects.all()
	return render(request, 'front_end/services.html', {'srv_list':list_srv})

def about_detail(request, abt_id):
	about_detail = About.objects.get(pk=abt_id)
	return render(request, 'front_end/detail.html', {'abt_det':about_detail})


def dashboard(request):
	return render(request, 'front_end/dashboard.html', {'mydbt':'Dashboard'})


def register(request):
	if request.method == 'POST':
		register_form = RegForm(request.POST)
		if register_form.is_valid():
			register_form.save()
			return redirect('revision_app:login')
	else:
		register_form = RegForm()
	return render(request, 'registration/register.html', {'reg':register_form})


