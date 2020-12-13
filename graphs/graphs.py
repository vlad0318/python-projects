import turtle
#start of positive x vairables vairables
x0=0
x1=3.5
x2=x1+3.5
x3=x2+3.5
x4=x3+3.5
x5=17.5
x6=x5+3.5
x7=x6+3.5
x8=x7+3.5
x9=x8+3.5
x10=35
x11=x10+3.5
x12=x11+3.5
x13=x12+3.5
x14=x13+3.5
x15=52.5
x20=70
x25=87.5
x30=105
x35=122.5
x40=140
x45=157.5
x50=175
x55=192.5
x60=210
x65=227.5
x70=245
x75=262.5
x80=280
x85=297.5
x90=315
x95=332.5
x100=350
#start of negative x vairables vairables
nx5=-17.5
nx10=-35
nx15=-52.5
nx20=-70
nx25=-87.5
nx30=-105
nx35=-122.5
nx40=-140
nx45=-157.5
nx50=-175
nx55=-192.5
nx60=-210
nx65=-227.5
nx70=-245
nx75=-262.5
nx80=-280
nx85=-297.5
nx90=-315
nx95=-332.5
nx100=-350
#start of positive y vairables vairables
y0=0
y5=17.5
y10=35
y15=52.5
y20=70
y25=87.5
y30=105
y35=122.5
y40=140
y45=157.5
y50=175
y55=192.5
y60=210
y65=227.5
y70=245
y75=262.5
y80=280
y85=297.5
y90=315
y95=332.5
y100=350
#start of negative y vairables vairables
ny5=-17.5
ny10=-35
ny15=-52.5
ny20=-70
ny25=-87.5
ny30=-105
ny35=-122.5
ny40=-140
ny45=-157.5
ny50=-175
ny55=-192.5
ny60=-210
ny65=-227.5
ny70=-245
ny75=-262.5
ny80=-280
ny85=-297.5
ny90=-315
ny95=-332.5
ny100=-350
#setup
clear_screen='y'
while clear_screen == 'y':
	turtle.pendown()
	turtle.setup(800,800)
	turtle.hideturtle()
	turtle.speed(0)
	#start of positive y graph
	turtle.penup()
	turtle.goto(x0,y0)
	turtle.dot()
	turtle.pendown()
	turtle.goto(0,350)
	turtle.goto(x0,y5)
	turtle.dot()
	turtle.penup()
	turtle.goto(10,y5-7.5)
	turtle.write("5")
	turtle.goto(x0,y10)
	turtle.dot()
	turtle.goto(10,y10-7.5)
	turtle.write("10")
	turtle.goto(x0,y15)
	turtle.dot()
	turtle.goto(10,y15-7.5)
	turtle.write("15")
	turtle.goto(x0,y20)
	turtle.dot()
	turtle.goto(10,x20-7.5)
	turtle.write("20")
	turtle.goto(x0,y25)
	turtle.dot()
	turtle.goto(10,x25-7.5)
	turtle.write("25")
	turtle.goto(x0,y30)
	turtle.dot()
	turtle.goto(10,x30-7.5)
	turtle.write("30")
	turtle.goto(x0,y35)
	turtle.dot()
	turtle.goto(10,x35-7.5)
	turtle.write("35")
	turtle.goto(x0,y40)
	turtle.dot()
	turtle.goto(10,x40-7.5)
	turtle.write("40")
	turtle.goto(x0,y45)
	turtle.dot()
	turtle.goto(10,x45-7.5)
	turtle.write("45")
	turtle.goto(x0,y50)
	turtle.dot()
	turtle.goto(10,x50-7.5)
	turtle.write("50")
	turtle.goto(x0,y55)
	turtle.dot()
	turtle.goto(10,x55-7.5)
	turtle.write("55")
	turtle.goto(x0,y60)
	turtle.dot()
	turtle.goto(10,x60-7.5)
	turtle.write("60")
	turtle.goto(x0,y65)
	turtle.dot()
	turtle.goto(10,x65-7.5)
	turtle.write("65")
	turtle.goto(x0,y70)
	turtle.dot()
	turtle.goto(10,x70-7.5)
	turtle.write("70")
	turtle.goto(x0,y75)
	turtle.dot()
	turtle.goto(10,x75-7.5)
	turtle.write("75")
	turtle.goto(x0,y80)
	turtle.dot()
	turtle.goto(10,x80-7.5)
	turtle.write("80")
	turtle.goto(x0,y85)
	turtle.dot()
	turtle.goto(10,x85-7.5)
	turtle.write("85")
	turtle.goto(x0,y90)
	turtle.dot()
	turtle.goto(10,x90-7.5)
	turtle.write("90")
	turtle.goto(x0,y95)
	turtle.dot()
	turtle.goto(10,x95-7.5)
	turtle.write("95")
	turtle.goto(x0,y100)
	turtle.dot()
	turtle.goto(10,x100-7.5)
	turtle.write("100")
	turtle.goto(0,0)
	turtle.pendown()	

	#start of negative y graph
	turtle.goto(0,-350)
	turtle.penup()
	turtle.goto(x0,ny5)
	turtle.dot()
	turtle.goto(10,ny5-7.5)
	turtle.write("-5")
	turtle.goto(x0,ny10)
	turtle.dot()
	turtle.goto(10,ny10-7.5)
	turtle.write("-10")
	turtle.goto(x0,ny15)
	turtle.dot()
	turtle.goto(10,ny15-7.5)
	turtle.write("-15")
	turtle.goto(x0,ny20)
	turtle.dot()
	turtle.goto(10,ny20-7.5)
	turtle.write("-20")
	turtle.goto(x0,ny25)
	turtle.dot()
	turtle.goto(10,ny25-7.5)
	turtle.write("-25")
	turtle.goto(x0,ny30)
	turtle.dot()
	turtle.goto(10,ny30-7.5)
	turtle.write("-30")
	turtle.goto(x0,ny35)
	turtle.dot()
	turtle.goto(10,ny35-7.5)
	turtle.write("-35")
	turtle.goto(x0,ny40)
	turtle.dot()
	turtle.goto(10,ny40-7.5)
	turtle.write("-40")
	turtle.goto(x0,ny45)
	turtle.dot()
	turtle.goto(10,ny45-7.5)
	turtle.write("-45")
	turtle.goto(x0,ny50)
	turtle.dot()
	turtle.goto(10,ny50-7.5)
	turtle.write("-50")
	turtle.goto(x0,ny55)
	turtle.dot()
	turtle.goto(10,ny55-7.5)
	turtle.write("-55")
	turtle.goto(x0,ny60)
	turtle.dot()
	turtle.goto(10,ny60-7.5)
	turtle.write("-60")
	turtle.goto(x0,ny65)
	turtle.dot()
	turtle.goto(10,ny65-7.5)
	turtle.write("-65")
	turtle.goto(x0,ny70)
	turtle.dot()
	turtle.goto(10,ny70-7.5)
	turtle.write("-70")
	turtle.goto(x0,ny75)
	turtle.dot()
	turtle.goto(10,ny75-7.5)
	turtle.write("-75")
	turtle.goto(x0,ny80)
	turtle.dot()
	turtle.goto(10,ny80-7.5)
	turtle.write("-80")
	turtle.goto(x0,ny85)
	turtle.dot()
	turtle.goto(10,ny85-7.5)
	turtle.write("-85")
	turtle.goto(x0,ny90)
	turtle.dot()
	turtle.goto(10,ny90-7.5)
	turtle.write("-90")
	turtle.goto(x0,ny95)
	turtle.dot()
	turtle.goto(10,ny95-7.5)
	turtle.write("-95")
	turtle.goto(x0,ny100)
	turtle.dot()
	turtle.goto(10,ny100-7.5)
	turtle.write("-100")	

	#start of positive x 
	turtle.goto(0,0)
	turtle.pendown()
	turtle.goto(350,0)
	turtle.penup()
	turtle.goto(x5,y0)
	turtle.dot()
	turtle.goto(x5-7.5,10)
	turtle.write("5")
	turtle.goto(x10,y0)
	turtle.dot()
	turtle.goto(x10-7.5,10)
	turtle.write("10")
	turtle.goto(x15,y0)
	turtle.dot()
	turtle.goto(x15-7.5,10)
	turtle.write("15")
	turtle.goto(x20,y0)
	turtle.dot()
	turtle.goto(x20-7.5,10)
	turtle.write("20")
	turtle.goto(x25,y0)
	turtle.dot()
	turtle.goto(x25-7.5,10)
	turtle.write("25")
	turtle.goto(x30,y0)
	turtle.dot()
	turtle.goto(x30-7.5,10)
	turtle.write("30")
	turtle.goto(x35,y0)
	turtle.dot()
	turtle.goto(x35-7.5,10)
	turtle.write("35")
	turtle.goto(x40,y0)
	turtle.dot()
	turtle.goto(x40-7.5,10)
	turtle.write("40")
	turtle.goto(x45,y0)
	turtle.dot()
	turtle.goto(x45-7.5,10)
	turtle.write("45")
	turtle.goto(x50,y0)
	turtle.dot()
	turtle.goto(x50-7.5,10)
	turtle.write("50")
	turtle.goto(x55,y0)
	turtle.dot()
	turtle.goto(x55-7.5,10)
	turtle.write("55")
	turtle.goto(x60,y0)
	turtle.dot()
	turtle.goto(x60-7.5,10)
	turtle.write("60")
	turtle.goto(x65,y0)
	turtle.dot()
	turtle.goto(x65-7.5,10)
	turtle.write("65")
	turtle.goto(x70,y0)
	turtle.dot()
	turtle.goto(x70-7.5,10)
	turtle.write("70")
	turtle.goto(x75,y0)
	turtle.dot()
	turtle.goto(x75-7.5,10)
	turtle.write("75")
	turtle.goto(x80,y0)
	turtle.dot()
	turtle.goto(x80-7.5,10)
	turtle.write("80")
	turtle.goto(x85,y0)
	turtle.dot()
	turtle.goto(x85-7.5,10)
	turtle.write("85")
	turtle.goto(x90,y0)
	turtle.dot()
	turtle.goto(x90-7.5,10)
	turtle.write("90")
	turtle.goto(x95,y0)
	turtle.dot()
	turtle.goto(x95-7.5,10)
	turtle.write("95")
	turtle.goto(x100,y0)
	turtle.dot()
	turtle.goto(x100-7.5,10)
	turtle.write("100")
	turtle.goto(0,0)
	turtle.pendown()	

	#start of negative x graph
	turtle.goto(-350,0)
	turtle.penup()
	turtle.goto(nx5,y0)
	turtle.dot()
	turtle.goto(nx5-7.5,10)
	turtle.write("-5")
	turtle.goto(nx10,y0)
	turtle.dot()
	turtle.goto(nx10-7.5,10)
	turtle.write("-10")
	turtle.goto(nx15,y0)
	turtle.dot()
	turtle.goto(nx15-7.5,10)
	turtle.write("-15")
	turtle.goto(nx20,y0)
	turtle.dot()
	turtle.goto(nx20-7.5,10)
	turtle.write("-20")
	turtle.goto(nx25,y0)
	turtle.dot()
	turtle.goto(nx25-7.5,10)
	turtle.write("-25")
	turtle.goto(nx30,y0)
	turtle.dot()
	turtle.goto(nx30-7.5,10)
	turtle.write("-30")
	turtle.goto(nx35,y0)
	turtle.dot()
	turtle.goto(nx35-7.5,10)
	turtle.write("-35")
	turtle.goto(nx40,y0)
	turtle.dot()
	turtle.goto(nx40-7.5,10)
	turtle.write("-40")
	turtle.goto(nx45,y0)
	turtle.dot()
	turtle.goto(nx45-7.5,10)
	turtle.write("-45")
	turtle.goto(nx50,y0)
	turtle.dot()
	turtle.goto(nx50-7.5,10)
	turtle.write("-50")
	turtle.goto(nx55,y0)
	turtle.dot()
	turtle.goto(nx55-7.5,10)
	turtle.write("-55")
	turtle.goto(nx60,y0)
	turtle.dot()
	turtle.goto(nx60-7.5,10)
	turtle.write("-60")
	turtle.goto(nx65,y0)
	turtle.dot()
	turtle.goto(nx65-7.5,10)
	turtle.write("-65")
	turtle.goto(nx70,y0)
	turtle.dot()
	turtle.goto(nx70-7.5,10)
	turtle.write("-70")
	turtle.goto(nx75,y0)
	turtle.dot()
	turtle.goto(nx75-7.5,10)
	turtle.write("-75")
	turtle.goto(nx80,y0)
	turtle.dot()
	turtle.goto(nx80-7.5,10)
	turtle.write("-80")
	turtle.goto(nx85,y0)
	turtle.dot()
	turtle.goto(nx85-7.5,10)
	turtle.write("-85")
	turtle.goto(nx90,y0)
	turtle.dot()
	turtle.goto(nx90-7.5,10)
	turtle.write("-90")
	turtle.goto(nx95,y0)
	turtle.dot()
	turtle.goto(nx95-7.5,10)
	turtle.write("-95")
	turtle.goto(nx100,y0)
	turtle.dot()
	turtle.goto(nx100-13.5,10)
	turtle.write("-100")
	turtle.pendown()	

	correct_answer='y'
	you_shur = 'y'
	while correct_answer == 'y' and you_shur == 'y':
		if you_shur == 'y':
			correct_answer='n'
			while correct_answer == 'n':
				shape = 0
				while shape != 1 and shape != 2 and shape != 3 and shape != 4:
					print('***************************')
					print('*hit 1 for a line        *')
					print('*hit 2 for a trianle      *')
					print('*hit 3 for a quadrelateral*')
					print('*hit 4 to exit            *')
					print('***************************')
					shape=int(input('what shape do you want to draw:'))
					if shape == 1:
						print('you picked the opption line')
					elif shape == 2:
						print('you picked the opption triangle')
					elif shape == 3:
						print('you picked the opption quadrelateral') 
					elif shape == 4:
						print('you chose the opption to exit')
					correct_answer = input('is this the opption that you wanted (answer in n for no or y for yes):')
					if shape == 1:
						x_var1 = int(input('what is your first x input: '))
						if x_var1 == 0:
							x_var1 = x0
						elif x_var1 ==  5 :
							x_var1 = x5
						elif x_var1 ==  10 :
							x_var1 = x10
						elif x_var1 ==  15 :
							x_var1 = x15
						elif x_var1 ==  20 :
							x_var1 = x20
						elif x_var1 ==  25 :
							x_var1 = x25
						elif x_var1 ==  30 :
							x_var1 = x30
						elif x_var1 ==  35 :
							x_var1 = x35
						elif x_var1 ==  40 :
							x_var1 = x40
						elif x_var1 ==  45 :
							x_var1 = x45
						elif x_var1 ==  50 :
							x_var1 = x50
						elif x_var1 ==  55 :
							x_var1 = x55
						elif x_var1 ==  60 :
							x_var1 = x60
						elif x_var1 ==  65 :
							x_var1 = x65
						elif x_var1 ==  70 :
							x_var1 = x70
						elif x_var1 ==  75 :
							x_var1 = x75
						elif x_var1 ==  80 :
							x_var1 = x80
						elif x_var1 ==  85 :
							x_var1 = x85
						elif x_var1 ==  90 :
							x_var1 = x90
						elif x_var1 ==  95 :
							x_var1 = x95
						elif x_var1 ==  100 :
							x_var1 = x100
						# negative x input var
						elif x_var1 == -5:
							x_var1 = nx5
						elif x_var1 == -10:
							x_var1 = nx10
						elif x_var1 == -15:
							x_var1 = nx15
						elif x_var1 == -20:
							x_var1 = nx20
						elif x_var1 == -25:
							x_var1 = nx25
						elif x_var1 == -30:
							x_var1 = nx30
						elif x_var1 == -35:
							x_var1 = nx35
						elif x_var1 == -40:
							x_var1 = nx40
						elif x_var1 == -45:
							x_var1 = nx45
						elif x_var1 == -50:
							x_var1 = nx50
						elif x_var1 == -55:
							x_var1 = nx55
						elif x_var1 == -60:
							x_var1 = nx60
						elif x_var1 == -65:
							x_var1 = nx65
						elif x_var1 == -70:
							x_var1 = nx70
						elif x_var1 == -75:
							x_var1 = nx75
						elif x_var1 == -80:
							x_var1 = nx80
						elif x_var1 == -85:
							x_var1 = nx85
						elif x_var1 == -90:
							x_var1 = nx90
						elif x_var1 == -95:
							x_var1 = nx95
						elif x_var1 == -100:
							x_var1 = nx100
						else:
							print('invalid input')		

						#start of y
						y_var1 = int(input('what is your first y input: '))
						#positive y input var
						if y_var1 == 0:
							y_var1 = y0
						elif y_var1 == 5:
							y_var1 = y5
						elif y_var1 == 10:
						    y_var1 = y10
						elif y_var1 == 15:
						    y_var1 = y15
						elif y_var1 == 20:
						    y_var1 = y20
						elif y_var1 == 25:
						    y_var1 = y25
						elif y_var1 == 30:
						    y_var1 = y30
						elif y_var1 == 35:
						    y_var1 = y35
						elif y_var1 == 40:
						    y_var1 = y40
						elif y_var1 == 45:
						    y_var1 = y45
						elif y_var1 == 50:
						    y_var1 = y50
						elif y_var1 == 55:
						    y_var1 = y55
						elif y_var1 == 60:
						    y_var1 = y60
						elif y_var1 == 65:
						    y_var1 = y65
						elif y_var1 == 70:
						    y_var1 = y70
						elif y_var1 == 75:
						    y_var1 = y75
						elif y_var1 == 80:
						    y_var1 = y80
						elif y_var1 == 85:
						    y_var1 = y85
						elif y_var1 == 90:
						    y_var1 = y90
						elif y_var1 == 95:
						    y_var1 = y95
						elif y_var1 == 100:
						    y_var1 = y100	
						#start of y negative
						elif y_var1 == -5:
							y_var1 = ny5
						elif y_var1 == -10:
							y_var1 = ny10
						elif y_var1 == -15:
							y_var1 = ny15
						elif y_var1 == -20:
							y_var1 = ny20
						elif y_var1 == -25:
							y_var1 = ny25
						elif y_var1 == -30:
							y_var1 = ny30
						elif y_var1 == -35:
							y_var1 = ny35
						elif y_var1 == -40:
							y_var1 = ny40
						elif y_var1 == -45:
							y_var1 = ny45
						elif y_var1 == -50:
							y_var1 = ny50
						elif y_var1 == -55:
							y_var1 = ny55
						elif y_var1 == -60:
							y_var1 = ny60
						elif y_var1 == -65:
							y_var1 = ny65
						elif y_var1 == -70:
							y_var1 = ny70
						elif y_var1 == -75:
							y_var1 = ny75
						elif y_var1 == -80:
							y_var1 = ny80
						elif y_var1 == -85:
							y_var1 = ny85
						elif y_var1 == -90:
							y_var1 = ny90
						elif y_var1 == -95:
							y_var1 = ny95
						elif y_var1 == -100:
							y_var1 = ny100
						else: 
							print('invalid input')
						turtle.penup()
						turtle.goto(x_var1,y_var1)
						turtle.pendown()
						turtle.dot()	

						x_var2 = int(input('what is your second x input: '))
						if x_var2 == 0:
							x_var2 = x0
						elif x_var2 ==  5 :
							x_var2 = x5
						elif x_var2 ==  10 :
							x_var2 = x10
						elif x_var2 ==  15 :
							x_var2 = x15
						elif x_var2 ==  20 :
							x_var2 = x20
						elif x_var2 ==  25 :
							x_var2 = x25
						elif x_var2 ==  30 :
							x_var2 = x30
						elif x_var2 ==  35 :
							x_var2 = x35
						elif x_var2 ==  40 :
							x_var2 = x40
						elif x_var2 ==  45 :
							x_var2 = x45
						elif x_var2 ==  50 :
							x_var2 = x50
						elif x_var2 ==  55 :
							x_var2 = x55
						elif x_var2 ==  60 :
							x_var2 = x60
						elif x_var2 ==  65 :
							x_var2 = x65
						elif x_var2 ==  70 :
							x_var2 = x70
						elif x_var2 ==  75 :
							x_var2 = x75
						elif x_var2 ==  80 :
							x_var2 = x80
						elif x_var2 ==  85 :
							x_var2 = x85
						elif x_var2 ==  90 :
							x_var2 = x90
						elif x_var2 ==  95 :
							x_var2 = x95
						elif x_var2 ==  100 :
							x_var2 = x100
						# negative x input var
						elif x_var2 == -5:
							x_var2 = nx5
						elif x_var2 == -10:
							x_var2 = nx10
						elif x_var2 == -15:
							x_var2 = nx15
						elif x_var2 == -20:
							x_var2 = nx20
						elif x_var2 == -25:
							x_var2 = nx25
						elif x_var2 == -30:
							x_var2 = nx30
						elif x_var2 == -35:
							x_var2 = nx35
						elif x_var2 == -40:
							x_var2 = nx40
						elif x_var2 == -45:
							x_var2 = nx45
						elif x_var2 == -50:
							x_var2 = nx50
						elif x_var2 == -55:
							x_var2 = nx55
						elif x_var2 == -60:
							x_var2 = nx60
						elif x_var2 == -65:
							x_var2 = nx65
						elif x_var2 == -70:
							x_var2 = nx70
						elif x_var2 == -75:
							x_var2 = nx75
						elif x_var2 == -80:
							x_var2 = nx80
						elif x_var2 == -85:
							x_var2 = nx85
						elif x_var2 == -90:
							x_var2 = nx90
						elif x_var2 == -95:
							x_var2 = nx95
						elif x_var2 == -100:
							x_var2 = nx100
						else:
							print('invalid input')		

						#start of y
						y_var2 = int(input('what is your second y input: '))
						#positive y input var
						if y_var2 == 0:
							y_var2 = y0
						elif y_var2 == 5:
							y_var2 = y5
						elif y_var2 == 10:
						    y_var2 = y10
						elif y_var2 == 15:
						    y_var2 = y15
						elif y_var2 == 20:
						    y_var2 = y20
						elif y_var2 == 25:
						    y_var2 = y25
						elif y_var2 == 30:
						    y_var2 = y30
						elif y_var2 == 35:
						    y_var2 = y35
						elif y_var2 == 40:
						    y_var2 = y40
						elif y_var2 == 45:
						    y_var2 = y45
						elif y_var2 == 50:
						    y_var2 = y50
						elif y_var2 == 55:
						    y_var2 = y55
						elif y_var2 == 60:
						    y_var2 = y60
						elif y_var2 == 65:
						    y_var2 = y65
						elif y_var2 == 70:
						    y_var2 = y70
						elif y_var2 == 75:
						    y_var2 = y75
						elif y_var2 == 80:
						    y_var2 = y80
						elif y_var2 == 85:
						    y_var2 = y85
						elif y_var2 == 90:
						    y_var2 = y90
						elif y_var2 == 95:
						    y_var2 = y95
						elif y_var2 == 100:
						    y_var2 = y100	
						#start of y negative
						elif y_var2 == -5:
							y_var2 = ny5
						elif y_var2 == -10:
							y_var2 = ny10
						elif y_var2 == -15:
							y_var2 = ny15
						elif y_var2 == -20:
							y_var2 = ny20
						elif y_var2 == -25:
							y_var2 = ny25
						elif y_var2 == -30:
							y_var2 = ny30
						elif y_var2 == -35:
							y_var2 = ny35
						elif y_var2 == -40:
							y_var2 = ny40
						elif y_var2 == -45:
							y_var2 = ny45
						elif y_var2 == -50:
							y_var2 = ny50
						elif y_var2 == -55:
							y_var2 = ny55
						elif y_var2 == -60:
							y_var2 = ny60
						elif y_var2 == -65:
							y_var2 = ny65
						elif y_var2 == -70:
							y_var2 = ny70
						elif y_var2 == -75:
							y_var2 = ny75
						elif y_var2 == -80:
							y_var2 = ny80
						elif y_var2 == -85:
							y_var2 = ny85
						elif y_var2 == -90:
							y_var2 = ny90
						elif y_var2 == -95:
							y_var2 = ny95
						elif y_var2 == -100:
							y_var2 = ny100
						else: 
							print('invalid input')
						turtle.goto(x_var2,y_var2)
						turtle.penup()
						turtle.dot()
					if shape == 2:
						x_var1 = int(input('what is your first x input: '))
						if x_var1 == 0:
							x_var1 = x0
						elif x_var1 ==  5 :
							x_var1 = x5
						elif x_var1 ==  10 :
							x_var1 = x10
						elif x_var1 ==  15 :
							x_var1 = x15
						elif x_var1 ==  20 :
							x_var1 = x20
						elif x_var1 ==  25 :
							x_var1 = x25
						elif x_var1 ==  30 :
							x_var1 = x30
						elif x_var1 ==  35 :
							x_var1 = x35
						elif x_var1 ==  40 :
							x_var1 = x40
						elif x_var1 ==  45 :
							x_var1 = x45
						elif x_var1 ==  50 :
							x_var1 = x50
						elif x_var1 ==  55 :
							x_var1 = x55
						elif x_var1 ==  60 :
							x_var1 = x60
						elif x_var1 ==  65 :
							x_var1 = x65
						elif x_var1 ==  70 :
							x_var1 = x70
						elif x_var1 ==  75 :
							x_var1 = x75
						elif x_var1 ==  80 :
							x_var1 = x80
						elif x_var1 ==  85 :
							x_var1 = x85
						elif x_var1 ==  90 :
							x_var1 = x90
						elif x_var1 ==  95 :
							x_var1 = x95
						elif x_var1 ==  100 :
							x_var1 = x100
						# negative x input var
						elif x_var1 == -5:
							x_var1 = nx5
						elif x_var1 == -10:
							x_var1 = nx10
						elif x_var1 == -15:
							x_var1 = nx15
						elif x_var1 == -20:
							x_var1 = nx20
						elif x_var1 == -25:
							x_var1 = nx25
						elif x_var1 == -30:
							x_var1 = nx30
						elif x_var1 == -35:
							x_var1 = nx35
						elif x_var1 == -40:
							x_var1 = nx40
						elif x_var1 == -45:
							x_var1 = nx45
						elif x_var1 == -50:
							x_var1 = nx50
						elif x_var1 == -55:
							x_var1 = nx55
						elif x_var1 == -60:
							x_var1 = nx60
						elif x_var1 == -65:
							x_var1 = nx65
						elif x_var1 == -70:
							x_var1 = nx70
						elif x_var1 == -75:
							x_var1 = nx75
						elif x_var1 == -80:
							x_var1 = nx80
						elif x_var1 == -85:
							x_var1 = nx85
						elif x_var1 == -90:
							x_var1 = nx90
						elif x_var1 == -95:
							x_var1 = nx95
						elif x_var1 == -100:
							x_var1 = nx100
						else:
							print('invalid input')		

						#start of y
						y_var1 = int(input('what is your first y input: '))
						#positive y input var
						if y_var1 == 0:
							y_var1 = y0
						elif y_var1 == 5:
							y_var1 = y5
						elif y_var1 == 10:
						    y_var1 = y10
						elif y_var1 == 15:
						    y_var1 = y15
						elif y_var1 == 20:
						    y_var1 = y20
						elif y_var1 == 25:
						    y_var1 = y25
						elif y_var1 == 30:
						    y_var1 = y30
						elif y_var1 == 35:
						    y_var1 = y35
						elif y_var1 == 40:
						    y_var1 = y40
						elif y_var1 == 45:
						    y_var1 = y45
						elif y_var1 == 50:
						    y_var1 = y50
						elif y_var1 == 55:
						    y_var1 = y55
						elif y_var1 == 60:
						    y_var1 = y60
						elif y_var1 == 65:
						    y_var1 = y65
						elif y_var1 == 70:
						    y_var1 = y70
						elif y_var1 == 75:
						    y_var1 = y75
						elif y_var1 == 80:
						    y_var1 = y80
						elif y_var1 == 85:
						    y_var1 = y85
						elif y_var1 == 90:
						    y_var1 = y90
						elif y_var1 == 95:
						    y_var1 = y95
						elif y_var1 == 100:
						    y_var1 = y100	
						#start of y negative
						elif y_var1 == -5:
							y_var1 = ny5
						elif y_var1 == -10:
							y_var1 = ny10
						elif y_var1 == -15:
							y_var1 = ny15
						elif y_var1 == -20:
							y_var1 = ny20
						elif y_var1 == -25:
							y_var1 = ny25
						elif y_var1 == -30:
							y_var1 = ny30
						elif y_var1 == -35:
							y_var1 = ny35
						elif y_var1 == -40:
							y_var1 = ny40
						elif y_var1 == -45:
							y_var1 = ny45
						elif y_var1 == -50:
							y_var1 = ny50
						elif y_var1 == -55:
							y_var1 = ny55
						elif y_var1 == -60:
							y_var1 = ny60
						elif y_var1 == -65:
							y_var1 = ny65
						elif y_var1 == -70:
							y_var1 = ny70
						elif y_var1 == -75:
							y_var1 = ny75
						elif y_var1 == -80:
							y_var1 = ny80
						elif y_var1 == -85:
							y_var1 = ny85
						elif y_var1 == -90:
							y_var1 = ny90
						elif y_var1 == -95:
							y_var1 = ny95
						elif y_var1 == -100:
							y_var1 = ny100
						else: 
							print('invalid input')
						turtle.penup()
						turtle.goto(x_var1,y_var1)
						turtle.pendown()
						turtle.dot()	

						x_var2 = int(input('what is your second x input: '))
						if x_var2 == 0:
							x_var2 = x0
						elif x_var2 ==  5 :
							x_var2 = x5
						elif x_var2 ==  10 :
							x_var2 = x10
						elif x_var2 ==  15 :
							x_var2 = x15
						elif x_var2 ==  20 :
							x_var2 = x20
						elif x_var2 ==  25 :
							x_var2 = x25
						elif x_var2 ==  30 :
							x_var2 = x30
						elif x_var2 ==  35 :
							x_var2 = x35
						elif x_var2 ==  40 :
							x_var2 = x40
						elif x_var2 ==  45 :
							x_var2 = x45
						elif x_var2 ==  50 :
							x_var2 = x50
						elif x_var2 ==  55 :
							x_var2 = x55
						elif x_var2 ==  60 :
							x_var2 = x60
						elif x_var2 ==  65 :
							x_var2 = x65
						elif x_var2 ==  70 :
							x_var2 = x70
						elif x_var2 ==  75 :
							x_var2 = x75
						elif x_var2 ==  80 :
							x_var2 = x80
						elif x_var2 ==  85 :
							x_var2 = x85
						elif x_var2 ==  90 :
							x_var2 = x90
						elif x_var2 ==  95 :
							x_var2 = x95
						elif x_var2 ==  100 :
							x_var2 = x100
						# negative x input var
						elif x_var2 == -5:
							x_var2 = nx5
						elif x_var2 == -10:
							x_var2 = nx10
						elif x_var2 == -15:
							x_var2 = nx15
						elif x_var2 == -20:
							x_var2 = nx20
						elif x_var2 == -25:
							x_var2 = nx25
						elif x_var2 == -30:
							x_var2 = nx30
						elif x_var2 == -35:
							x_var2 = nx35
						elif x_var2 == -40:
							x_var2 = nx40
						elif x_var2 == -45:
							x_var2 = nx45
						elif x_var2 == -50:
							x_var2 = nx50
						elif x_var2 == -55:
							x_var2 = nx55
						elif x_var2 == -60:
							x_var2 = nx60
						elif x_var2 == -65:
							x_var2 = nx65
						elif x_var2 == -70:
							x_var2 = nx70
						elif x_var2 == -75:
							x_var2 = nx75
						elif x_var2 == -80:
							x_var2 = nx80
						elif x_var2 == -85:
							x_var2 = nx85
						elif x_var2 == -90:
							x_var2 = nx90
						elif x_var2 == -95:
							x_var2 = nx95
						elif x_var2 == -100:
							x_var2 = nx100
						else:
							print('invalid input')		

						#start of y
						y_var2 = int(input('what is your second y input: '))
						#positive y input var
						if y_var2 == 0:
							y_var2 = y0
						elif y_var2 == 5:
							y_var2 = y5
						elif y_var2 == 10:
						    y_var2 = y10
						elif y_var2 == 15:
						    y_var2 = y15
						elif y_var2 == 20:
						    y_var2 = y20
						elif y_var2 == 25:
						    y_var2 = y25
						elif y_var2 == 30:
						    y_var2 = y30
						elif y_var2 == 35:
						    y_var2 = y35
						elif y_var2 == 40:
						    y_var2 = y40
						elif y_var2 == 45:
						    y_var2 = y45
						elif y_var2 == 50:
						    y_var2 = y50
						elif y_var2 == 55:
						    y_var2 = y55
						elif y_var2 == 60:
						    y_var2 = y60
						elif y_var2 == 65:
						    y_var2 = y65
						elif y_var2 == 70:
						    y_var2 = y70
						elif y_var2 == 75:
						    y_var2 = y75
						elif y_var2 == 80:
						    y_var2 = y80
						elif y_var2 == 85:
						    y_var2 = y85
						elif y_var2 == 90:
						    y_var2 = y90
						elif y_var2 == 95:
						    y_var2 = y95
						elif y_var2 == 100:
						    y_var2 = y100	
						#start of y negative
						elif y_var2 == -5:
							y_var2 = ny5
						elif y_var2 == -10:
							y_var2 = ny10
						elif y_var2 == -15:
							y_var2 = ny15
						elif y_var2 == -20:
							y_var2 = ny20
						elif y_var2 == -25:
							y_var2 = ny25
						elif y_var2 == -30:
							y_var2 = ny30
						elif y_var2 == -35:
							y_var2 = ny35
						elif y_var2 == -40:
							y_var2 = ny40
						elif y_var2 == -45:
							y_var2 = ny45
						elif y_var2 == -50:
							y_var2 = ny50
						elif y_var2 == -55:
							y_var2 = ny55
						elif y_var2 == -60:
							y_var2 = ny60
						elif y_var2 == -65:
							y_var2 = ny65
						elif y_var2 == -70:
							y_var2 = ny70
						elif y_var2 == -75:
							y_var2 = ny75
						elif y_var2 == -80:
							y_var2 = ny80
						elif y_var2 == -85:
							y_var2 = ny85
						elif y_var2 == -90:
							y_var2 = ny90
						elif y_var2 == -95:
							y_var2 = ny95
						elif y_var2 == -100:
							y_var2 = ny100
						else: 
							print('invalid input')
						turtle.goto(x_var2,y_var2)
						turtle.dot()
						#shape 3
						x_var3 = int(input('what is your second x input: '))
						if x_var3 == 0:
							x_var3 = x0
						elif x_var3 ==  5 :
							x_var3 = x5
						elif x_var3 ==  10 :
							x_var3 = x10
						elif x_var3 ==  15 :
							x_var3 = x15
						elif x_var3 ==  20 :
							x_var3 = x20
						elif x_var3 ==  25 :
							x_var3 = x25
						elif x_var3 ==  30 :
							x_var3 = x30
						elif x_var3 ==  35 :
							x_var3 = x35
						elif x_var3 ==  40 :
							x_var3 = x40
						elif x_var3 ==  45 :
							x_var3 = x45
						elif x_var3 ==  50 :
							x_var3 = x50
						elif x_var3 ==  55 :
							x_var3 = x55
						elif x_var3 ==  60 :
							x_var3 = x60
						elif x_var3 ==  65 :
							x_var3 = x65
						elif x_var3 ==  70 :
							x_var3 = x70
						elif x_var3 ==  75 :
							x_var3 = x75
						elif x_var3 ==  80 :
							x_var3 = x80
						elif x_var3 ==  85 :
							x_var3 = x85
						elif x_var3 ==  90 :
							x_var3 = x90
						elif x_var3 ==  95 :
							x_var3 = x95
						elif x_var3 ==  100 :
							x_var3 = x100
						# negative x input var
						elif x_var3 == -5:
							x_var3 = nx5
						elif x_var3 == -10:
							x_var3 = nx10
						elif x_var3 == -15:
							x_var3 = nx15
						elif x_var3 == -20:
							x_var3 = nx20
						elif x_var3 == -25:
							x_var3 = nx25
						elif x_var3 == -30:
							x_var3 = nx30
						elif x_var3 == -35:
							x_var3 = nx35
						elif x_var3 == -40:
							x_var3 = nx40
						elif x_var3 == -45:
							x_var3 = nx45
						elif x_var3 == -50:
							x_var3 = nx50
						elif x_var3 == -55:
							x_var3 = nx55
						elif x_var3 == -60:
							x_var3 = nx60
						elif x_var3 == -65:
							x_var3 = nx65
						elif x_var3 == -70:
							x_var3 = nx70
						elif x_var3 == -75:
							x_var3 = nx75
						elif x_var3 == -80:
							x_var3 = nx80
						elif x_var3 == -85:
							x_var3 = nx85
						elif x_var3 == -90:
							x_var3 = nx90
						elif x_var3 == -95:
							x_var3 = nx95
						elif x_var3 == -100:
							x_var3 = nx100
						else:
							print('invalid input')		

						#start of y
						y_var3 = int(input('what is your second y input: '))
						#positive y input var
						if y_var3 == 0:
							y_var3 = y0
						elif y_var3 == 5:
							y_var3 = y5
						elif y_var3 == 10:
						    y_var3 = y10
						elif y_var3 == 15:
						    y_var3 = y15
						elif y_var3 == 20:
						    y_var3 = y20
						elif y_var3 == 25:
						    y_var3 = y25
						elif y_var3 == 30:
						    y_var3 = y30
						elif y_var3 == 35:
						    y_var3 = y35
						elif y_var3 == 40:
						    y_var3 = y40
						elif y_var3 == 45:
						    y_var3 = y45
						elif y_var3 == 50:
						    y_var3 = y50
						elif y_var3 == 55:
						    y_var3 = y55
						elif y_var3 == 60:
						    y_var3 = y60
						elif y_var3 == 65:
						    y_var3 = y65
						elif y_var3 == 70:
						    y_var3 = y70
						elif y_var3 == 75:
						    y_var3 = y75
						elif y_var3 == 80:
						    y_var3 = y80
						elif y_var3 == 85:
						    y_var3 = y85
						elif y_var3 == 90:
						    y_var3 = y90
						elif y_var3 == 95:
						    y_var3 = y95
						elif y_var3 == 100:
						    y_var3 = y100	
						#start of y negative
						elif y_var3 == -5:
							y_var3 = ny5
						elif y_var3 == -10:
							y_var3 = ny10
						elif y_var3 == -15:
							y_var3 = ny15
						elif y_var3 == -20:
							y_var3 = ny20
						elif y_var3 == -25:
							y_var3 = ny25
						elif y_var3 == -30:
							y_var3 = ny30
						elif y_var3 == -35:
							y_var3 = ny35
						elif y_var3 == -40:
							y_var3 = ny40
						elif y_var3 == -45:
							y_var3 = ny45
						elif y_var3 == -50:
							y_var3 = ny50
						elif y_var3 == -55:
							y_var3 = ny55
						elif y_var3 == -60:
							y_var3 = ny60
						elif y_var3 == -65:
							y_var3 = ny65
						elif y_var3 == -70:
							y_var3 = ny70
						elif y_var3 == -75:
							y_var3 = ny75
						elif y_var3 == -80:
							y_var3 = ny80
						elif y_var3 == -85:
							y_var3 = ny85
						elif y_var3 == -90:
							y_var3 = ny90
						elif y_var3 == -95:
							y_var3 = ny95
						elif y_var3 == -100:
							y_var3 = ny100
						else: 
							print('invalid input')
						turtle.goto(x_var3,y_var3)
						turtle.dot()
						turtle.goto(x_var1,y_var1)
						turtle.penup()

						#start of the quadrelateral
					if shape == 3:
						x_var1 = int(input('what is your first x input: '))
						if x_var1 == 0:
							x_var1 = x0
						elif x_var1 ==  5 :
							x_var1 = x5
						elif x_var1 ==  10 :
							x_var1 = x10
						elif x_var1 ==  15 :
							x_var1 = x15
						elif x_var1 ==  20 :
							x_var1 = x20
						elif x_var1 ==  25 :
							x_var1 = x25
						elif x_var1 ==  30 :
							x_var1 = x30
						elif x_var1 ==  35 :
							x_var1 = x35
						elif x_var1 ==  40 :
							x_var1 = x40
						elif x_var1 ==  45 :
							x_var1 = x45
						elif x_var1 ==  50 :
							x_var1 = x50
						elif x_var1 ==  55 :
							x_var1 = x55
						elif x_var1 ==  60 :
							x_var1 = x60
						elif x_var1 ==  65 :
							x_var1 = x65
						elif x_var1 ==  70 :
							x_var1 = x70
						elif x_var1 ==  75 :
							x_var1 = x75
						elif x_var1 ==  80 :
							x_var1 = x80
						elif x_var1 ==  85 :
							x_var1 = x85
						elif x_var1 ==  90 :
							x_var1 = x90
						elif x_var1 ==  95 :
							x_var1 = x95
						elif x_var1 ==  100 :
							x_var1 = x100
						# negative x input var
						elif x_var1 == -5:
							x_var1 = nx5
						elif x_var1 == -10:
							x_var1 = nx10
						elif x_var1 == -15:
							x_var1 = nx15
						elif x_var1 == -20:
							x_var1 = nx20
						elif x_var1 == -25:
							x_var1 = nx25
						elif x_var1 == -30:
							x_var1 = nx30
						elif x_var1 == -35:
							x_var1 = nx35
						elif x_var1 == -40:
							x_var1 = nx40
						elif x_var1 == -45:
							x_var1 = nx45
						elif x_var1 == -50:
							x_var1 = nx50
						elif x_var1 == -55:
							x_var1 = nx55
						elif x_var1 == -60:
							x_var1 = nx60
						elif x_var1 == -65:
							x_var1 = nx65
						elif x_var1 == -70:
							x_var1 = nx70
						elif x_var1 == -75:
							x_var1 = nx75
						elif x_var1 == -80:
							x_var1 = nx80
						elif x_var1 == -85:
							x_var1 = nx85
						elif x_var1 == -90:
							x_var1 = nx90
						elif x_var1 == -95:
							x_var1 = nx95
						elif x_var1 == -100:
							x_var1 = nx100
						else:
							print('invalid input')		

						#start of y
						y_var1 = int(input('what is your first y input: '))
						#positive y input var
						if y_var1 == 0:
							y_var1 = y0
						elif y_var1 == 5:
							y_var1 = y5
						elif y_var1 == 10:
						    y_var1 = y10
						elif y_var1 == 15:
						    y_var1 = y15
						elif y_var1 == 20:
						    y_var1 = y20
						elif y_var1 == 25:
						    y_var1 = y25
						elif y_var1 == 30:
						    y_var1 = y30
						elif y_var1 == 35:
						    y_var1 = y35
						elif y_var1 == 40:
						    y_var1 = y40
						elif y_var1 == 45:
						    y_var1 = y45
						elif y_var1 == 50:
						    y_var1 = y50
						elif y_var1 == 55:
						    y_var1 = y55
						elif y_var1 == 60:
						    y_var1 = y60
						elif y_var1 == 65:
						    y_var1 = y65
						elif y_var1 == 70:
						    y_var1 = y70
						elif y_var1 == 75:
						    y_var1 = y75
						elif y_var1 == 80:
						    y_var1 = y80
						elif y_var1 == 85:
						    y_var1 = y85
						elif y_var1 == 90:
						    y_var1 = y90
						elif y_var1 == 95:
						    y_var1 = y95
						elif y_var1 == 100:
						    y_var1 = y100	
						#start of y negative
						elif y_var1 == -5:
							y_var1 = ny5
						elif y_var1 == -10:
							y_var1 = ny10
						elif y_var1 == -15:
							y_var1 = ny15
						elif y_var1 == -20:
							y_var1 = ny20
						elif y_var1 == -25:
							y_var1 = ny25
						elif y_var1 == -30:
							y_var1 = ny30
						elif y_var1 == -35:
							y_var1 = ny35
						elif y_var1 == -40:
							y_var1 = ny40
						elif y_var1 == -45:
							y_var1 = ny45
						elif y_var1 == -50:
							y_var1 = ny50
						elif y_var1 == -55:
							y_var1 = ny55
						elif y_var1 == -60:
							y_var1 = ny60
						elif y_var1 == -65:
							y_var1 = ny65
						elif y_var1 == -70:
							y_var1 = ny70
						elif y_var1 == -75:
							y_var1 = ny75
						elif y_var1 == -80:
							y_var1 = ny80
						elif y_var1 == -85:
							y_var1 = ny85
						elif y_var1 == -90:
							y_var1 = ny90
						elif y_var1 == -95:
							y_var1 = ny95
						elif y_var1 == -100:
							y_var1 = ny100
						else: 
							print('invalid input')
						turtle.penup()
						turtle.goto(x_var1,y_var1)
						turtle.pendown()
						turtle.dot()	

						x_var2 = int(input('what is your second x input: '))
						if x_var2 == 0:
							x_var2 = x0
						elif x_var2 ==  5 :
							x_var2 = x5
						elif x_var2 ==  10 :
							x_var2 = x10
						elif x_var2 ==  15 :
							x_var2 = x15
						elif x_var2 ==  20 :
							x_var2 = x20
						elif x_var2 ==  25 :
							x_var2 = x25
						elif x_var2 ==  30 :
							x_var2 = x30
						elif x_var2 ==  35 :
							x_var2 = x35
						elif x_var2 ==  40 :
							x_var2 = x40
						elif x_var2 ==  45 :
							x_var2 = x45
						elif x_var2 ==  50 :
							x_var2 = x50
						elif x_var2 ==  55 :
							x_var2 = x55
						elif x_var2 ==  60 :
							x_var2 = x60
						elif x_var2 ==  65 :
							x_var2 = x65
						elif x_var2 ==  70 :
							x_var2 = x70
						elif x_var2 ==  75 :
							x_var2 = x75
						elif x_var2 ==  80 :
							x_var2 = x80
						elif x_var2 ==  85 :
							x_var2 = x85
						elif x_var2 ==  90 :
							x_var2 = x90
						elif x_var2 ==  95 :
							x_var2 = x95
						elif x_var2 ==  100 :
							x_var2 = x100
						# negative x input var
						elif x_var2 == -5:
							x_var2 = nx5
						elif x_var2 == -10:
							x_var2 = nx10
						elif x_var2 == -15:
							x_var2 = nx15
						elif x_var2 == -20:
							x_var2 = nx20
						elif x_var2 == -25:
							x_var2 = nx25
						elif x_var2 == -30:
							x_var2 = nx30
						elif x_var2 == -35:
							x_var2 = nx35
						elif x_var2 == -40:
							x_var2 = nx40
						elif x_var2 == -45:
							x_var2 = nx45
						elif x_var2 == -50:
							x_var2 = nx50
						elif x_var2 == -55:
							x_var2 = nx55
						elif x_var2 == -60:
							x_var2 = nx60
						elif x_var2 == -65:
							x_var2 = nx65
						elif x_var2 == -70:
							x_var2 = nx70
						elif x_var2 == -75:
							x_var2 = nx75
						elif x_var2 == -80:
							x_var2 = nx80
						elif x_var2 == -85:
							x_var2 = nx85
						elif x_var2 == -90:
							x_var2 = nx90
						elif x_var2 == -95:
							x_var2 = nx95
						elif x_var2 == -100:
							x_var2 = nx100
						else:
							print('invalid input')		

						#start of y
						y_var2 = int(input('what is your second y input: '))
						#positive y input var
						if y_var2 == 0:
							y_var2 = y0
						elif y_var2 == 5:
							y_var2 = y5
						elif y_var2 == 10:
						    y_var2 = y10
						elif y_var2 == 15:
						    y_var2 = y15
						elif y_var2 == 20:
						    y_var2 = y20
						elif y_var2 == 25:
						    y_var2 = y25
						elif y_var2 == 30:
						    y_var2 = y30
						elif y_var2 == 35:
						    y_var2 = y35
						elif y_var2 == 40:
						    y_var2 = y40
						elif y_var2 == 45:
						    y_var2 = y45
						elif y_var2 == 50:
						    y_var2 = y50
						elif y_var2 == 55:
						    y_var2 = y55
						elif y_var2 == 60:
						    y_var2 = y60
						elif y_var2 == 65:
						    y_var2 = y65
						elif y_var2 == 70:
						    y_var2 = y70
						elif y_var2 == 75:
						    y_var2 = y75
						elif y_var2 == 80:
						    y_var2 = y80
						elif y_var2 == 85:
						    y_var2 = y85
						elif y_var2 == 90:
						    y_var2 = y90
						elif y_var2 == 95:
						    y_var2 = y95
						elif y_var2 == 100:
						    y_var2 = y100	
						#start of y negative
						elif y_var2 == -5:
							y_var2 = ny5
						elif y_var2 == -10:
							y_var2 = ny10
						elif y_var2 == -15:
							y_var2 = ny15
						elif y_var2 == -20:
							y_var2 = ny20
						elif y_var2 == -25:
							y_var2 = ny25
						elif y_var2 == -30:
							y_var2 = ny30
						elif y_var2 == -35:
							y_var2 = ny35
						elif y_var2 == -40:
							y_var2 = ny40
						elif y_var2 == -45:
							y_var2 = ny45
						elif y_var2 == -50:
							y_var2 = ny50
						elif y_var2 == -55:
							y_var2 = ny55
						elif y_var2 == -60:
							y_var2 = ny60
						elif y_var2 == -65:
							y_var2 = ny65
						elif y_var2 == -70:
							y_var2 = ny70
						elif y_var2 == -75:
							y_var2 = ny75
						elif y_var2 == -80:
							y_var2 = ny80
						elif y_var2 == -85:
							y_var2 = ny85
						elif y_var2 == -90:
							y_var2 = ny90
						elif y_var2 == -95:
							y_var2 = ny95
						elif y_var2 == -100:
							y_var2 = ny100
						else: 
							print('invalid input')
						turtle.goto(x_var2,y_var2)
						turtle.dot()
						#shape 3
						x_var3 = int(input('what is your second x input: '))
						if x_var3 == 0:
							x_var3 = x0
						elif x_var3 ==  5 :
							x_var3 = x5
						elif x_var3 ==  10 :
							x_var3 = x10
						elif x_var3 ==  15 :
							x_var3 = x15
						elif x_var3 ==  20 :
							x_var3 = x20
						elif x_var3 ==  25 :
							x_var3 = x25
						elif x_var3 ==  30 :
							x_var3 = x30
						elif x_var3 ==  35 :
							x_var3 = x35
						elif x_var3 ==  40 :
							x_var3 = x40
						elif x_var3 ==  45 :
							x_var3 = x45
						elif x_var3 ==  50 :
							x_var3 = x50
						elif x_var3 ==  55 :
							x_var3 = x55
						elif x_var3 ==  60 :
							x_var3 = x60
						elif x_var3 ==  65 :
							x_var3 = x65
						elif x_var3 ==  70 :
							x_var3 = x70
						elif x_var3 ==  75 :
							x_var3 = x75
						elif x_var3 ==  80 :
							x_var3 = x80
						elif x_var3 ==  85 :
							x_var3 = x85
						elif x_var3 ==  90 :
							x_var3 = x90
						elif x_var3 ==  95 :
							x_var3 = x95
						elif x_var3 ==  100 :
							x_var3 = x100
						# negative x input var
						elif x_var3 == -5:
							x_var3 = nx5
						elif x_var3 == -10:
							x_var3 = nx10
						elif x_var3 == -15:
							x_var3 = nx15
						elif x_var3 == -20:
							x_var3 = nx20
						elif x_var3 == -25:
							x_var3 = nx25
						elif x_var3 == -30:
							x_var3 = nx30
						elif x_var3 == -35:
							x_var3 = nx35
						elif x_var3 == -40:
							x_var3 = nx40
						elif x_var3 == -45:
							x_var3 = nx45
						elif x_var3 == -50:
							x_var3 = nx50
						elif x_var3 == -55:
							x_var3 = nx55
						elif x_var3 == -60:
							x_var3 = nx60
						elif x_var3 == -65:
							x_var3 = nx65
						elif x_var3 == -70:
							x_var3 = nx70
						elif x_var3 == -75:
							x_var3 = nx75
						elif x_var3 == -80:
							x_var3 = nx80
						elif x_var3 == -85:
							x_var3 = nx85
						elif x_var3 == -90:
							x_var3 = nx90
						elif x_var3 == -95:
							x_var3 = nx95
						elif x_var3 == -100:
							x_var3 = nx100
						else:
							print('invalid input')		

						#start of y
						y_var3 = int(input('what is your second y input: '))
						#positive y input var
						if y_var3 == 0:
							y_var3 = y0
						elif y_var3 == 5:
							y_var3 = y5
						elif y_var3 == 10:
						    y_var3 = y10
						elif y_var3 == 15:
						    y_var3 = y15
						elif y_var3 == 20:
						    y_var3 = y20
						elif y_var3 == 25:
						    y_var3 = y25
						elif y_var3 == 30:
						    y_var3 = y30
						elif y_var3 == 35:
						    y_var3 = y35
						elif y_var3 == 40:
						    y_var3 = y40
						elif y_var3 == 45:
						    y_var3 = y45
						elif y_var3 == 50:
						    y_var3 = y50
						elif y_var3 == 55:
						    y_var3 = y55
						elif y_var3 == 60:
						    y_var3 = y60
						elif y_var3 == 65:
						    y_var3 = y65
						elif y_var3 == 70:
						    y_var3 = y70
						elif y_var3 == 75:
						    y_var3 = y75
						elif y_var3 == 80:
						    y_var3 = y80
						elif y_var3 == 85:
						    y_var3 = y85
						elif y_var3 == 90:
						    y_var3 = y90
						elif y_var3 == 95:
						    y_var3 = y95
						elif y_var3 == 100:
						    y_var3 = y100	
						#start of y negative
						elif y_var3 == -5:
							y_var3 = ny5
						elif y_var3 == -10:
							y_var3 = ny10
						elif y_var3 == -15:
							y_var3 = ny15
						elif y_var3 == -20:
							y_var3 = ny20
						elif y_var3 == -25:
							y_var3 = ny25
						elif y_var3 == -30:
							y_var3 = ny30
						elif y_var3 == -35:
							y_var3 = ny35
						elif y_var3 == -40:
							y_var3 = ny40
						elif y_var3 == -45:
							y_var3 = ny45
						elif y_var3 == -50:
							y_var3 = ny50
						elif y_var3 == -55:
							y_var3 = ny55
						elif y_var3 == -60:
							y_var3 = ny60
						elif y_var3 == -65:
							y_var3 = ny65
						elif y_var3 == -70:
							y_var3 = ny70
						elif y_var3 == -75:
							y_var3 = ny75
						elif y_var3 == -80:
							y_var3 = ny80
						elif y_var3 == -85:
							y_var3 = ny85
						elif y_var3 == -90:
							y_var3 = ny90
						elif y_var3 == -95:
							y_var3 = ny95
						elif y_var3 == -100:
							y_var3 = ny100
						else: 
							print('invalid input')
						turtle.goto(x_var3,y_var3)
						turtle.dot()

						y_var4 = int(input('what is your second y input: '))
						#positive y input var
						if y_var4 == 0:
							y_var4 = y0
						elif y_var4 == 5:
							y_var4 = y5
						elif y_var4 == 10:
						    y_var4 = y10
						elif y_var4 == 15:
						    y_var4 = y15
						elif y_var4 == 20:
						    y_var4 = y20
						elif y_var4 == 25:
						    y_var4 = y25
						elif y_var4 == 30:
						    y_var4 = y30
						elif y_var4 == 35:
						    y_var4 = y35
						elif y_var4 == 40:
						    y_var4 = y40
						elif y_var4 == 45:
						    y_var4 = y45
						elif y_var4 == 50:
						    y_var4 = y50
						elif y_var4 == 55:
						    y_var4 = y55
						elif y_var4 == 60:
						    y_var4 = y60
						elif y_var4 == 65:
						    y_var4 = y65
						elif y_var4 == 70:
						    y_var4 = y70
						elif y_var4 == 75:
						    y_var4 = y75
						elif y_var4 == 80:
						    y_var4 = y80
						elif y_var4 == 85:
						    y_var4 = y85
						elif y_var4 == 90:
						    y_var4 = y90
						elif y_var4 == 95:
						    y_var4 = y95
						elif y_var4 == 100:
						    y_var4 = y100	
						#start of y negative
						elif y_var4 == -5:
							y_var4 = ny5
						elif y_var4 == -10:
							y_var4 = ny10
						elif y_var4 == -15:
							y_var4 = ny15
						elif y_var4 == -20:
							y_var4 = ny20
						elif y_var4 == -25:
							y_var4 = ny25
						elif y_var4 == -30:
							y_var4 = ny30
						elif y_var4 == -35:
							y_var4 = ny35
						elif y_var4 == -40:
							y_var4 = ny40
						elif y_var4 == -45:
							y_var4 = ny45
						elif y_var4 == -50:
							y_var4 = ny50
						elif y_var4 == -55:
							y_var4 = ny55
						elif y_var4 == -60:
							y_var4 = ny60
						elif y_var4 == -65:
							y_var4 = ny65
						elif y_var4 == -70:
							y_var4 = ny70
						elif y_var4 == -75:
							y_var4 = ny75
						elif y_var4 == -80:
							y_var4 = ny80
						elif y_var4 == -85:
							y_var4 = ny85
						elif y_var4 == -90:
							y_var4 = ny90
						elif y_var4 == -95:
							y_var4 = ny95
						elif y_var4 == -100:
							y_var4 = ny100
						else: 
							print('invalid input')

						x_var4 = int(input('what is your second y input: '))
						#positive y input var
						if x_var4 == 0:
							x_var4 = x0
						elif x_var4 == 5:
							x_var4 = x5
						elif x_var4 == 10:
						    x_var4 = x10
						elif x_var4 == 15:
						    x_var4 = x15
						elif x_var4 == 20:
						    x_var4 = x20
						elif x_var4 == 25:
						    x_var4 = x25
						elif x_var4 == 30:
						    x_var4 = x30
						elif x_var4 == 35:
						    x_var4 = x35
						elif x_var4 == 40:
						    x_var4 = x40
						elif x_var4 == 45:
						    x_var4 = x45
						elif x_var4 == 50:
						    x_var4 = x50
						elif x_var4 == 55:
						    x_var4 = x55
						elif x_var4 == 60:
						    x_var4 = x60
						elif x_var4 == 65:
						    x_var4 = x65
						elif x_var4 == 70:
						    x_var4 = x70
						elif x_var4 == 75:
						    x_var4 = x75
						elif x_var4 == 80:
						    x_var4 = x80
						elif x_var4 == 85:
						    x_var4 = x85
						elif x_var4 == 90:
						    x_var4 = x90
						elif x_var4 == 95:
						    x_var4 = x95
						elif x_var4 == 100:
						    x_var4 = x100	
						#start of y negative
						elif x_var4 == -5:
							x_var4 = nx5
						elif x_var4 == -10:
							x_var4 = nx10
						elif x_var4 == -15:
							x_var4 = nx15
						elif x_var4 == -20:
							x_var4 = nx20
						elif x_var4 == -25:
							x_var4 = nx25
						elif x_var4 == -30:
							x_var4 = nx30
						elif x_var4 == -35:
							x_var4 = nx35
						elif x_var4 == -40:
							x_var4 = nx40
						elif x_var4 == -45:
							x_var4 = nx45
						elif x_var4 == -50:
							x_var4 = nx50
						elif x_var4 == -55:
							x_var4 = nx55
						elif x_var4 == -60:
							x_var4 = nx60
						elif x_var4 == -65:
							x_var4 = nx65
						elif x_var4 == -70:
							x_var4 = nx70
						elif x_var4 == -75:
							x_var4 = nx75
						elif x_var4 == -80:
							x_var4 = nx80
						elif x_var4 == -85:
							x_var4 = nx85
						elif x_var4 == -90:
							x_var4 = nx90
						elif x_var4 == -95:
							x_var4 = nx95
						elif x_var4 == -100:
							x_var4 = nx100
						else: 
							print('invalid input')

						turtle.pendown()
						turtle.goto(x_var4,y_var4)
						turtle.dot()
						turtle.goto(x_var1,y_var1)
						turtle.penup()
		if shape == 4:
			you_shur = 'n'
			correct_answer='y'
		else:
			you_shur = input('do you want to draw another shape (answer in y or n):')
	clear_screen=input('do you want to clear screen (answer in y or n):')
	if clear_screen == 'y':
		turtle.clear()
print('you quit the program')  
