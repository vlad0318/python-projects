text = input('input text :')
split_times=len(text)
charecter_write=0
with open('variebles.py','w') as f:
	for var in range(split_times):
		var+=1
		part1=str('var')
		part3=str('\'')
		part4=('=')
		part2=text[charecter_write]
		f.write(part1)
		f.write(str(var))
		f.write(part4)
		f.write(part3)
		f.write(part2)
		f.write(part3)
		f.write('\n')
		charecter_write+=1