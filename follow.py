
prod = [
		'S=Aa','A=BD','B=b|$','D=d|$'
	   ]

variables = ['S','A','B','D']
terminals = ['$','+','-','*','/','a','b','d']

def follow(var,prod):	
	if var==prod[0][0] :
		return ('$')
	for i in range(0 ,len(prod)):
		if var in prod[i]:	
			if prod[i].index(var)==(len(prod[i])-1) :
				return first(prod[i][0],prod)		
			elif prod[i][prod[i].index(var)+1] in terminals :
				return (prod[i][prod[i].index(var)+1]) 
			elif prod[i][prod[i].index(var)+1]  in variables :
				if prod[0][0] == var :
					return ('$')
				else:
					return first(prod[i][prod[i].index(var)+1],prod)		#Omkar thawakar
																			#reg No : 2015bcs003
			else :															#Roll No : A-04
				return None

def first(var,prod):
	for i in range(len(prod)):
		if prod[i][0] == var :
			if '|' in prod[i] :
				if prod[i][2] not in variables :
					if prod[i][prod[i].index('|')+1] not in variables :
						return prod[i][2] ,prod[i][prod[i].index('|')+1]
					else:
						return prod[i][2] , first(prod[i][prod[i].index('|')+1] , prod)
				else:	
					if prod[i][prod[i].index('|')+1] not in variables :
						return first(prod[i][2],prod) ,prod[i][prod[i].index('|')+1]
					else:
						return first(prod[i][2],prod) , first(prod[i][prod[i].index('|')+1] , prod)
			else:			
				if prod[i][2] not in variables:
					return prod[i][2]
				else:
					return first(prod[i][2],prod)

print("Productions are : ",prod)
while(True):
	fo = str(input("enter prod to find follow : "))
	res = follow(fo,prod)
	print("follow of %s is %s "%(fo,res))