import random
import string

def generate(length, lower_case, upper_case, numeric, special_character):
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

	password = random.choices(password, k=int(length))

	password = ''.join(password)
	
	return password


