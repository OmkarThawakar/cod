prod = [
		'S=Aa','A=BD','B=b|$','D=d|$'
	   ]

variables = ['S','A','B','D']
terminals = ['$','+','-','*','/','a','b','d']
'''
no_prod = int(input("enter no of productions : "))

for i in range(no_prod):
	production = str(input("enter production : "))
	prod.append(production)
'''
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
					return first(prod[i][2],prod)							#Name : Omkar Thawakar
																			#Reg No :2015BCS003
print("Productions are : ",prod)											#Roll No : A-04

while(True):
	fi = str(input("enter prod to find follow : "))
	res = first(fi,prod)
	print("First of %s is %s "%(fi,res))