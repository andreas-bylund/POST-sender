#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
from random import randint
import requests
import string
import random

'''
Script som skickar en massa POST Request till en adress som fiskade efter
mailadress från Skövde Högskola.

Några saker man kan förbättra:
	- Multithreading, gör så att fler random data skickas till adressen. Just nu
	ligger det på 2-3 POST Requests i sekunden.
	- Någon form av proxy lösning så personen ifråga kan inte sortera ut datan
	genom IP-adressen.
'''


#  name: getUsername()
#  @param
#  @return String, a random username (a12anduw@student.his.se)
def getUsername():

	mail = "@student.his.se"

	year = [10, 11, 12, 13, 14, 15, 16, 17, 18]
	letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "v", "w"]

	#Hämta ett random tal
	ran_int = randomNumber(0, len(letters))

	#Första bokstaven i användarnamnet (Index 0)
	x = letters[ran_int]

	#Hämta året som eleven började skolan (Index 1-2)
	ran = randomNumber(0, len(year))
	xyear = year[ran]

	#Random bokstav (Index 3)
	h = randomNumber(0, len(letters))
	x1 = letters[h]

	#Random bokstav (Index 3)
	h = randomNumber(0, len(letters))
	x2 = letters[h]

	#Random bokstav (Index 4)
	h = randomNumber(0, len(letters))
	x3 = letters[h]

	#Random bokstav (Index 5)
	h = randomNumber(0, len(letters))
	x4 = letters[h]

	#Random bokstav (Index 6)
	h = randomNumber(0, len(letters))
	x5 = letters[h]

	username = str(x) + str(xyear) + str(x1) + str(x2) + str(x3) + str(x4) + str(x5) + mail

	return username


#  name: getPassword()
#  @param
#  @return String, a random password
def getPassword():

	N = randomNumber(7, 15)

	pwd =  ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(N))

	return pwd

#  name: randomNumber()
#  @param
#  @return Int, random number between "min" and "max"
def randomNumber(min, max):
	maxnumber = max - 1
	return randint(min, maxnumber)

def main(args):

	#Url to send POST-request to
	url = ""

	#Number of iterations counter
	x = 0

	for x in range(10000):
		#Counter
		x = x + 1

		data = {'wb_input_0': 'his.se', 'wb_input_1' : getUsername(), 'wb_input_2' : getPassword(), 'wb_input_3' : 'student', 'wb_form_id' : 'c75823e9'}
		r = requests.post(url, data=data)

		print "Antal: "  + str(x)
		print(r.status_code, r.reason)



if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
