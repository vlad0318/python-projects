from variebles import *
def encryption():
	print('hi')

times = 1 
file = open("variebles.py","r") 
Counter = 0
Content = file.read() 
CoList = Content.split("\n") 
for i in CoList: 
    if i: 
        Counter += 1

while times <= Counter:
	varh =str('var')
	print(varh)
	times = times+1