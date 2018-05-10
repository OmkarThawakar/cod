#ip = str(input("Enter a string : "))
ip = '( a + b ) / ( c * d ) * ( e - f )'

#ip = 'a + b / c * d * e - f'

var = ['P','Q','R','S','T','U','V']
op = ['+','-','/','*']

Stack = []

def infixToPostfix(infixexpr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    Stack = []
    postfixList = []
    tokenList = infixexpr.split()

    for token in tokenList:
        if token in "abcdefghijklmnopqrstuvwxyz" or token in "0123456789":
            postfixList.append(token)
        elif token == '(':
            Stack.append(token)                                         #Name : Omkar Thawakar
        elif token == ')':                                              #Reg No : 2015BCS003
            topToken = Stack.pop()                                      #Roll No : A-04
            while topToken != '(':
                postfixList.append(topToken)
                topToken = Stack.pop()
        else:
            while (len(Stack) != 0) and (prec[Stack[len(Stack)-1]] >= prec[token]):
                  postfixList.append(Stack.pop())
            Stack.append(token)

    while len(Stack) != 0 :
        postfixList.append(Stack.pop())
    return " ".join(postfixList)

def countOp(string):
    count = 0
    for i in range(len(string)):
        if string[i] in  op :
            count = count + 1
    return count

exp = infixToPostfix(ip)
print(exp)

test = exp
j=0
result = []
def xyz(test,j,result):
    try :
        for i in range(len(test)) :    
            if test[i] in op :
                result.append(var[j]+'='+test[i-4]+test[i]+test[i-2])
                test = test.replace(test[test.index(test[i])-4 : test.index(test[i])+1 ],var[j])
                j+=1
                if j==countOp(exp)+1 :
                    exit(0)
                xyz(test,j,result)
    except:
        pass
xyz(test,j,result)

print("Ipnput string is : ",ip)
print("Three Address Code is : ",result[:countOp(exp)])

