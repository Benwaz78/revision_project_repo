from django.shortcuts import render
from revision_app.forms import(DjangoForm1, FormWiget, FormValidation)


def django_form1(request):
	form1 = DjangoForm1()
	return render(request, 'front_end/form1.html', {'my_form':form1})


def django_form2(request):
	form2 = DjangoForm1()

	if request.method == 'POST':
		form2 = DjangoForm1(request.POST)
		if form2.is_valid():
			print('Name ', form2.cleaned_data['name'])
			print('Subject ', form2.cleaned_data['subject'])
			print('Email ', form2.cleaned_data['email'])
			print('Message ', form2.cleaned_data['message'])
	else:
		form2 = DjangoForm1()
	return render(request, 'front_end/form2.html', {'my_form2':form2})

def form_widget(request):
	form_widget = FormWiget()
	return render(request, 'front_end/form_widget.html', {'form_wid':form_widget})

def form_validators(request):
	if request.method == 'POST':
		hold_data = FormValidation(request.POST)
		if hold_data.is_valid():
			print('Name', hold_data.cleaned_data['name'])
			print('Subject', hold_data.cleaned_data['subject'])
			print('Email', hold_data.cleaned_data['email'])
			print('Message', hold_data.cleaned_data['message'])
	else:
		hold_data = FormValidation()
	return render(request, 'front_end/form_validator.html', {'my_form_data':hold_data})


