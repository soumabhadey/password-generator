from django.shortcuts import render
from . import generate_passwords


def home(request):
	context = {
		"length": 8,
		"lower_case": True,
		"upper_case": True,
		"numeric": True,
		"special_character": True,
	}
	if request.method == "POST":
		length = int(request.POST.get("length"))
		lower_case =  "lower_case" in request.POST
		upper_case = "upper_case" in request.POST
		numeric = "numeric" in request.POST
		special_character = "special_character" in request.POST
		password = generate_passwords.generate(length, lower_case, upper_case, numeric, special_character)
		context = {
			"password": password,
			"length": length,
			"lower_case": lower_case,
			"upper_case": upper_case,
			"numeric": numeric,
			"special_character": special_character,
		}
	return render(request, "index.html", context)