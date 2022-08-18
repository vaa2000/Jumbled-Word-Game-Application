from django.shortcuts import render
from random import choice, sample
city_names = [ "Mumbai", "Delhi", "Chennai", "Pune", "Bangalore", "Lucknow", "Hyderabad", "Nasik", "Surat", "Vadodara", "Thane", "Vashi"]

word = ""

def home(request):
	global word
	word = choice(city_names)
	jum = sample(word, len(word))
	jum_word = "".join(jum)
	return render(request, "home.html", {"jum_word":jum_word})

def check(request):
	global word
	ans = request.GET.get("ans")
	if ans == word:
		msg = "u r right\nword was " + word
	else:
		msg = "u r wrong\nword was " + word
	return render(request, "check.html", {"msg":msg})
