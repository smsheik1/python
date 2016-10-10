heads = 0
tails = 0
import random

for attempt in range(1,5001):

	random_num = round(random.random())
	if(random_num ==1):
		tails+= 1
		print 'attempt: '+ str(attempt) + ' Tails! Count is: '+ str(tails)
	else:
		heads+=1
		print  'attempt:' + str(attempt)+ ' Head! Count is: '+ str(heads)