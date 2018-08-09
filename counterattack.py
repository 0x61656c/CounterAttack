import requests
import random
import string
import json

def randomizeCase(string):
	"""
	Function: 
		Randomizes the case of a string input. Used to prevent automated filtering of counterattack information.
		Example: input password12 will convert to any of the following examples:

		pAssword12, PASsword12, PasSSWORD12, passwoRD12, etc.

	Notes:
		Return type: string
		Dependencies: 
			libraries: random, string
	"""
	limit = random.randrange(0, int(len(string)/2))
	spots = []
	result = ""

	while len(spots) <= limit:
		value = random.randrange(0, int(len(string) - 1))
		if value not in spots:
			spots.append(value)

	for char in range(len(string)):
		
		if char not in spots:
			ext = str(string[char])
			result += ext

		else:
			ext = str(string[char]).upper()
			result += ext

	return result

def unameGenerator(lim):
	"""
	Function: 
		Generates usernames for ints in range [0, limit]
		each element in the output username array is of the following form

		[uname_base][int extension][generic provider]

		Ex: aaron23@gmail.com, michelle56@yahoo.com, etc.

	Notes: 
		Return type: array 
		Dependencies: 
			data: names.json
			library: random


	"""
	uname_base = json.loads(open('names.json').read())
	#print(uname_base[1000])

	result = []

	for element in range(lim):
		uname_ext = "%i" %(random.random() * 100)

		uname_composite = uname_base[element].lower() +\
		uname_ext +\
		random.choice(["@gmail.com", "@yahoo.com","@aol.com","@hotmail.com","@icloud.com"])

		result.append(uname_composite)

	return result

def passGenerator(lim):
	"""
	Function: 
		Generates passwords for ints in range [0,limit]
		each element in the output password array is of the following form:

		[pwd_base][pwd_extension]

		Ex: carbon14, oxygen8, etc.

		Each password is also put through the randomized capitalization function, 
		so inputs are sometimes convoluted to 

		CarbON14, OXYGen8, etc.

	Notes:
		Return type: array
		Dependencies: 
			data: passwords.json
			libaray: random

	"""
	pwd_base = json.loads(open('passwords.json').read())

	result = []

	for element in range(lim):
		pwd_ext = "%i" %(random.random() * 100)
		new_pwd_base = randomizeCase(pwd_base[element])
		pwd_composite = new_pwd_base + pwd_ext

		result.append(pwd_composite)

	return result

def sessionGenerator(lim):
	"""
	Function: 
		Generates usernames and passwords for ints in range(0, limit)

		Ex:

		(uname = aalebel33, pwd = carbon14)

	Notes:
		Return type: Array of tuples
		Dependencies: 
			function: passGenerator
			function: unameGenerator
	"""
	unames = unameGenerator(lim)
	pwds = passGenerator(lim)

	result = zip(unames,pwds)

	return list(result)
def submitData(payload = ("username","password"), url = ""):
	"""
	Function: 
		completes a single form submission requiring username and password input.
		Does not allow redirects to increase speed of form submission.

	Notes: 
		Input types: 
			payload = tuple
			url = string
		Return types:
			None
		Dependencies:
			Library: Requests
	"""
	uname = payload[0]
	pwd = payload[1]
	print(uname)
	print(pwd)
	print(url)

	uname_field = 'email'#insert uname var label
	pwd_field = 'last_name' #insert pwd var label
	post = '_POST'

	requests.post(url, allow_redirects = False, data={
		uname_field: uname,
		pwd_field: pwd,
		'_POST': ['submit'],
		
	})

def counterAttack(url = "", limit = 0):
	"""
	Function: 
		Attack script. Generates a list of uname and pwd tuples and passes them through the submit data function.
		Currently limited by the size of the data input for usernames, which is 2283. However, this function can be run multiple times
		and yield different results. 

	Notes:
		Dependencies: 
			Functions: submitData
	"""
	_yield = sessionGenerator(limit)
	index = 0

	for session in _yield:
		index += 1
		submitData(session)
		print("Submitted session #%i" %index)

	return None


###Test Cases. Not comprehensive because I dont intend on this being a multi-day project.
def testUnameGenerator():
	print(unameGenerator(1000))

def testPassGenerator():
	print(passGenerator(9))
	
def testRandomizeCase():
	print(randomizeCase("helloworld"))
	
def testSessionGenerator():
	print(sessionGenerator(1000))

def testSubmitData():
	submitData(("aalebel33","carbon14"),"https://consulting.cryptonettech.com/submit.php")

def testAll():
	#testUnameGenerator()
	#testRandomizeCase()
	#testPassGenerator()
	#testSessionGenerator()
	testSubmitData()
	pass

def main():
	testAll()

if __name__ == "__main__":
	main()

