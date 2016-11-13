from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django import forms

class NameForm(forms.Form):
    username = forms.CharField(
    	widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'GitHub username'}),
    	label='', 
    	max_length=200
    )

# Create your views here.
def index(request):
	if request.method == 'POST':
		form = NameForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			return HttpResponseRedirect('stats/'+ username)
	else:
		form = NameForm()
	return render(request, 'application/index.html', {'form': form})

def stats(request):
	return redirect("/")

def username(request, username):
	context = {
		'username' : username
	}
	return render(request, 'application/stats.html', context)