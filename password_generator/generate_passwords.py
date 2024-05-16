import random
import string

def generate(length, lower_case, upper_case, numeric, special_character):
	password = []
	if lower_case:
		password.extend(string.ascii_lowercase)
	if upper_case:
		password.extend(string.ascii_uppercase)
	if numeric:
		password.extend(string.digits)
	if special_character:
		password.extend(string.punctuation)

	random.shuffle(password)

	password_length = length - 5

	password = random.choices(password, k=password_length)

	
	if lower_case:
		password.insert(random.randint(0, password_length), random.choice(string.ascii_lowercase))
		password_length += 1
	if upper_case:
		password.insert(random.randint(0, password_length), random.choice(string.ascii_uppercase))
		password_length += 1
	if numeric:
		password.insert(random.randint(0, password_length), random.choice(string.digits))
		password_length += 1
	if special_character:
		password.insert(random.randint(0, password_length), random.choice(string.punctuation))
		password_length += 1

	if password_length < length - 1:
		diff = length - 1 - password_length
		if special_character:
			password[:0] = random.choices(string.punctuation, k=diff)
		elif numeric:
			password[:0] = random.choices(string.digits, k=diff)
		elif upper_case:
			password[:0] = random.choices(string.ascii_uppercase, k=diff)
		elif lower_case:
			password[:0] = random.choices(string.ascii_lowercase, k=diff)
		
		password_length = length - 1


	if lower_case and upper_case :
		password.insert(0, random.choice(string.ascii_letters))
	elif lower_case :
		password.insert(0, random.choice(string.ascii_lowercase))

	password_length = length

	password = ''.join(password)

	return password


