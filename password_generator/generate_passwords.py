import random
import string

def generate(length, lower_case, upper_case, numeric, special_character):
	length = int(length)
	password = ""
	
	if lower_case:
		password = password + string.ascii_lowercase
	if upper_case:
		password = password + string.ascii_uppercase
	if numeric:
		password = password + string.digits
	if special_character:
		password = password + string.punctuation
	
	password = list(password)
	random.shuffle(password)

	password = random.choices(password, k=int(length)-5)

	password = ''.join(password)
	
	if lower_case:
		password = password + random.choice(string.ascii_lowercase)
	if upper_case:
		password = random.choice(string.ascii_uppercase) + password
	if numeric:
		password = password + random.choice(string.digits)
	if special_character:
		password = random.choice(string.punctuation) + password

	if len(password) < length:
		diff = length - len(password)
		if special_character:
			password = ''.join(random.choices(string.punctuation, k=diff)) + password
		if numeric:
			password = password + ''.join(random.choices(string.digits, k=diff))
		if upper_case:
			password = ''.join(random.choices(string.ascii_uppercase, k=diff)) + password
		if lower_case:
			password = password + ''.join(random.choices(string.ascii_lowercase, k=diff))


	if lower_case and upper_case :
		password = random.choice(string.ascii_letters) + password
	elif lower_case :
		password = random.choice(string.ascii_lowercase) + password

	return password


