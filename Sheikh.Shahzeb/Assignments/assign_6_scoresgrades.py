def grades():
	grade=input("This is a letter Grade Generator, what number grade did you get...")
	if(grade>59 and grade<=69):
		print 'you recieved an D'
	elif(grade>69 and grade<=79):
		print 'you recieved a C'
	elif(grade>79 and grade<=89):
		print 'you recieved a B'
	elif(grade>89 and grade<=100):
		print 'you recieved an A'
	elif(grade>100):
		print 'you recieved higher than an A!'
	else:
		print 'you recieved an F. Better luck next time!'

for grade in range(0,10): 
	grades()

	

