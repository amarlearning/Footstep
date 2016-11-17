from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django import forms
import urllib2
import json

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

# https://api.github.com/users/amarlearning/events?page=4

def username(request, username):
	url = 'https://api.github.com/users/' + username + '/events'
	serialized_data = urllib2.urlopen(url).read().decode("utf-8")
	data = json.loads(serialized_data)

	tabs = {
		'CommitCommentEvent' : 'Comments',
		'IssueCommentEvent' : 'Comments',
		'PullRequestReviewCommentEvent' : 'Comments'
	}
	context = {
		'username' : username,
		'json' : data,
		'tabs' : tabs
	}
	return render(request, 'application/stats.html', context)