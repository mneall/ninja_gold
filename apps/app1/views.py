from django.shortcuts import render, redirect, HttpResponse
import random, datetime

def index(request):
	if not 'gold' in request.session:
		request.session['gold'] = 0
	if not 'log' in request.session:
		request.session['log'] = []
# create dictionary to pass to index template containing score and log
	context = {'gold': request.session['gold'], 'log': request.session['log']}
	print "Debug"
	return render(request, "app1/index.html", context)

def process(request):
	if request.method == "POST":
		building = request.POST['building']
		if request.POST['building'] == 'farm':
			earnings = random.randrange(10, 20)
		elif request.POST['building'] == 'cave':
			earnings = random.randrange(5, 10)
		elif request.POST['building'] == 'house':
			earnings = random.randrange(2, 5)
		elif request.POST['building'] == 'casino':
			earnings = random.randrange(-50, 50)	
		else:
			# ignore unknown building types
			pass

		msg = ""
		now = str(datetime.datetime.now())
		if earnings > 0:
			msg = "Earned " + str(earnings) + " golds from the " + building + "! (" + now + ")"
			styleClass="green"
		else:
			msg = "You should really stop gambling... (" + now + ")"
			styleClass="red"
			# insert comment into log containing message and class for p-tag
		request.session['log'].insert(0, {"class": styleClass, "message": msg})
			# get new score and return it
		request.session['gold']+=earnings

	return redirect('/')

def reset(request):
	request.session.clear()
	return redirect('/')
