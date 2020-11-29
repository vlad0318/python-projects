import random
i='y'
while i=='y' or i=='yes' or i=='Yes' :
	randome_number=random.randrange(0,3)
	randome_number=randome_number+1
	print('you are playing rock paper scissors')
	print('your opptions are:')
	print('*******************')
	print('*1 is for rock    *')
	print('*2 is for paper   *')
	print('*3 is for scissors*')
	print('*******************')
	user_number=int(input('what is your number:'))
	if user_number == randome_number:
		print('you tied')
		print(randome_number)
	elif randome_number == 3 and user_number == 1:
		print('you won')
		print(randome_number)
	elif randome_number == 1  and user_number == 2:
		print('you won')
		print(randome_number)
	elif randome_number ==2  and user_number == 3:
		print('you won')
		print(randome_number)
	elif randome_number ==3  and user_number == 2:
		print('you lost')
		print(randome_number)
	elif randome_number ==1  and user_number == 3:
		print('you lost')
		print(randome_number)
	elif randome_number ==2  and user_number == 1:
		print('you lost')
		print(randome_number)
	else:
		print('invalid input')
		print(randome_number)
	i=input('do you want to play again:')