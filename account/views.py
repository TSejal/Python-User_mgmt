from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def account_register(request):
	if request.method == 'POST':
		user_details=request.POST
		fnm=user_details.get('fname')
		lnm=user_details.get('lname')
		email=user_details.get('email')
		unm=user_details.get('username')
		psw=user_details.get('password')
		re_psw=user_details.get('con_password')
		if psw==re_psw:
			user=User.objects.create_user(unm,email,psw)
			user.save()
			return HttpResponseRedirect('/account/login/')
		else:
			return render(request, 'register.html')
		
		
	else:
		return render(request, 'register.html')


def account_login(request):
	print "from log in view"
	form_data=request.POST
	nm=form_data.get('username')
	psw=form_data.get('password')
	user = authenticate(username=nm, password=psw)
	if user is not None:
		login(request, user)
		return HttpResponseRedirect('/account/home/')
	else:
		return render(request, 'logIn.html')

def account_home(request):
	user = request.user.username
	return render(request, 'home.html', {'name':user})


def account_logout(request):
	logout(request)
	return HttpResponseRedirect('/account/login/')
	#return render(request, 'logout.html')
