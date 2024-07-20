from django.shortcuts import render, redirect
from . import generate_passwords

def home(request):
	if request.method == "POST":
		length = int(request.POST.get("length"))
		lower_case = "lower_case" in request.POST
		upper_case = "upper_case" in request.POST
		numeric = "numeric" in request.POST
		special_character = "special_character" in request.POST
		number_of_passwords = int(request.POST.get("number_of_passwords"))
		passwords = []
		
		for _ in range(number_of_passwords):
			passwords.append(generate_passwords.generate(length, lower_case, upper_case, numeric, special_character))
			 
		
		request.session['context'] = {
			"passwords": passwords,
			"length": length,
			"lower_case": lower_case,
			"upper_case": upper_case,
			"numeric": numeric,
			"special_character": special_character,
			"number_of_passwords": number_of_passwords,
		}

		return redirect('home')

	context = request.session.pop('context', {
		"length": 8,
		"lower_case": True,
		"upper_case": True,
		"numeric": True,
		"special_character": True,
		"number_of_passwords": 5,
	})

	return render(request, "index.html", context)


