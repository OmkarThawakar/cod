grammer = {'S':'aBDh','B':'cC','C':'bC|$','D':'EF','E':'g|$','F':'f|$'}
variables = ['S','A','B','C','D','E','F']
terminals = ['$','a','b','c','g','f']
stack = '$'
ip =  str(input("Enter string : "))  # 'acgfh$' #input string to accept 
stack = grammer['S']+stack
print("Stack\tInput_String\n")
while ip!='$' and stack!='$' :
    if ip[0]==stack[0]:
        print(stack.replace(stack[0],'')+"\t"+ip.replace(ip[0],''))
        stack = stack.replace(stack[0],'')
        ip = ip.replace(ip[0],'')
    elif ip[0] != stack[0]:
        if stack[0] in variables :
            if ip[0] in grammer[stack[0]] and ip[0]==grammer[stack[0]][0] :
                if '$' in grammer[stack[0]] :    
                    stack = stack.replace(stack[0],grammer[stack[0]][:grammer[stack[0]].index('$')-1])
                    print(stack+"\t"+ip)
                elif '$' not in grammer[stack[0]] :
                    stack = stack.replace(stack[0],grammer[stack[0]])
                    print(stack+"\t"+ip)
            elif '$' in stack[0] :
                stack = stack.replace(stack[0],'')
            elif ip[0] in grammer[stack[0]] :
                if '$' in grammer[stack[0]] :    
                    stack = stack.replace(stack[0],grammer[stack[0]][:grammer[stack[0]].index('$')-1])
                    print(stack+"\t"+ip)
                elif '$' not in grammer[stack[0]] :
                    stack = stack.replace(stack[0],grammer[stack[0]])
            elif ip[0] not in grammer[stack[0]] and '$' in grammer[stack[0]] :
                stack = stack.replace(stack[0],'')
                print(stack+"\t"+ip)
            elif ip[0] not in grammer[stack[0]] and '$' not in grammer[stack[0]] :
                stack = stack.replace(stack[0],grammer[stack[0]])
                print(stack+"\t"+ip)       
if ip == '$' and stack == '$' :      
	print("String Accepted!!!!!") 
else :
	print("String Rejected$$$$$")
    
