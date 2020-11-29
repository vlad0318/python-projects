import random
wana_play='y'
print('you are playing guess the number (it is from 1-100)')
while wana_play == 'y':
	randome_number=random.randrange(0,100)
	correct='n'
	while  correct != 'y':
		user_input=int(input('what is your number:'))
		if user_input < randome_number:
			print('to low')
		elif user_input > randome_number:
			print('to high')
		elif user_input == randome_number:
			print('you won!!!!!!!!!!!!')
			correct='y'
		else:
			print('invalid input')
	wana_play=input('do you want to play again:')
print('you quit the game')