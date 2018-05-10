prod = [
        'S=ab|D','A=b|d','B=b|a','D=d|$'
       ]

variables = ['S','A','B','D']
terminals = ['$','+','-','*','/','a','b','d']

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

def follow(var,prod):                                                       #name : Omkar Thawakar
    if var==prod[0][0] :                                                    #reg no :2015bcs003
        return ('$')                                                        #roll no : A-04
    for i in range(0 ,len(prod)):
        if var in prod[i]:  
            if prod[i].index(var)==(len(prod[i])-1) :
                return follow(prod[i][0],prod)
            elif prod[i][prod[i].index(var)+1] in terminals :
                return (prod[i][prod[i].index(var)+1]) 
            elif prod[i][prod[i].index(var)+1]  in variables :
                if prod[0][0] == var :
                    return ('$')
                else:
                    if '$' in first(prod[i][prod[i].index(var)+1],prod) :
                        if (prod[i].index(var)+1 == len(prod[i])-1) :
                            return first(prod[i][prod[i].index(var)+1],prod)[0] , follow(prod[i][0],prod)
                    return first(prod[i][prod[i].index(var)+1],prod)
            else :
                return None

print("Productions are : ",prod)

print("variable :: " , "First :: " , "Follow :: ")
for i in prod :
    print(i[0] , " : : " , first(i[0] , prod) , " : : " , follow(i[0],prod))
    
ppt = {'S':{'a':[],'b':[],'d':[],'$':[]} , 
       'A':{'a':[],'b':[],'d':[],'$':[]} ,
       'B':{'a':[],'b':[],'d':[],'$':[]} ,
       'D':{'a':[],'b':[],'d':[],'$':[]}
      }

for var in prod:
    for i in first(var[0],prod) :
        if i == '$' :
            for j in follow(var[0],prod) :
                ppt[var[0]][j].append(var[0]+'=$')
        else :
            if '$' in var :
                ppt[var[0]][i].append(var[:var.index('|')])
            else :
                ppt[var[0]][i].append(var)
                
print("Predictive Parsing Table is Given By : ")
for i in ppt :
    print(i ," :: ", ppt[i])