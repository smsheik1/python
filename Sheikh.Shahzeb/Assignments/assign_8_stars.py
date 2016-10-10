'''def draw_stars():
	x=[4,6,1,3,5,7,25]
	print str(x)
draw_stars()'''

def draw_stars2():
	x="*"
	z=[4,6,1,3,5,7,25]
	arr1 =[4,"Tom",1,"Michael",5,7,"Jimmy Smith"]
	'''print 4*x
	print 6*x
	print x
	print 3*x
	print 5*x
	print 7*x
	print 25*x'''
	for var in arr1:
		if type(var)==int:
			print "*" * var 
		if type(var)==str:
			print var[0] * len(var)
draw_stars2()


