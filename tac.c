/*
Aim-: Write a C or C++ program for Three Address Code generation for the arithmetic, assignment and relational statements.
*/
/* ****** PROGRAM ****** */
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
char exp[10], exp1[10], exp2[10], id1[5], op[5], id2[5];
int n=40, ch, i, j, len, addr=100;
void strrev(char a[]){
	len = strlen(a);
	char b[len];
	for(i=len-1; i>=0; i--)
		b[len-i-1] = a[i];
	for(i=0; i<len; i++)
		a[i] = b[i];
}
void pm(){
	strrev(exp);
	j=len-i-1;
	strncat(exp1, exp, j);
	strrev(exp1);
	printf("temp=%s\ntemp1=%c%ctemp\n",exp1, exp[j+1], exp[j]);
}
void divs(){
	strncat(exp1,exp,i+2);
	printf("temp=%s\ntemp1=temp%c%c\n",exp1, exp[i+2], exp[i+3]);
}
void plus(){
	strncat(exp1,exp,i+2);
	printf("temp=%s\ntemp1=temp%c%c\n",exp1, exp[i+2], exp[i+3]);
}
void assignTAC(){
	printf("Enter the string with assignment operator:\n");
	scanf("%s",&exp);
	int i=0;
	while(exp[i]!='='){
		i++;
    }
    exp2[0]='\0';
    strncat(exp2,exp,i);
    len=strlen(exp);
    strrev(exp);
    exp1[0]='\0';
    strncat(exp1,exp,len-(i+1));
    strrev(exp1);
    printf("temp=%s\n", exp1);
    printf("%s=temp\n", exp2);
}
void arithmTAC(){
	printf("Enter the expression with arithmetic operator:");
	scanf("%s",exp);
	len=strlen(exp);
	exp1[0]='\0';
	for(i=0;i<len;i++){
		if(exp[i]=='+'||exp[i]=='-'){
			if(exp[i+2]=='/'||exp[i+2]=='*'){
				pm();
				break;
			}else{
				plus();
				break;
			}
		}else if(exp[i]=='/'||exp[i]=='*'){
			divs();
			break;
		}
	}
}
void relatnTAC(){
	printf("Enter the expression with relational statement:\n");
	scanf("%s%s%s",&id1,&op,&id2);
	if(((strcmp(op,"<")==0)||(strcmp(op,">")==0)||(strcmp(op,"<=")==0)||(strcmp(op,">=")==0)||(strcmp(op,"==")==0)||(strcmp(op,"!=")==0))==0)
		printf("Expression is error");
	else{
		printf("%d\tif %s%s%s goto %d\n",addr,id1,op,id2,addr+3);
		addr++;
		printf("%d\t T:=0\n",addr);
		addr++;
		printf("%d\t goto %d\n",addr,addr+2);
		addr++;
		printf("%d\t T:=1\n",addr);
	}
}
void main(){
   	printf("Enter your choice\t1:Assignment\t2:Arithmetic\t3:Relational\t4:exit\n");
    scanf("%d",&ch);
	switch(ch){
     	case 1: assignTAC();
     		break;
     	case 2: arithmTAC();
     		break;
     	case 3: relatnTAC();
     		break;
     	case 4: exit(0);
     		break;
     	default: printf("Not a valid choice! Exiting...\nExited\n");
     		exit(0);
     		break;
   }
}
/* ****** OUTPUT ******
lab1-16@lab1-16:~/Harshad$ gcc P11.c
lab1-16@lab1-16:~/Harshad$ ./a.out
Enter your choice	1:Assignment	2:Arithmetic	3:Relational	4:exit
1
Enter the string with assignment operator:
a=b
temp=b
a=temp

lab1-16@lab1-16:~/Harshad$ ./a.out
Enter your choice	1:Assignment	2:Arithmetic	3:Relational	4:exit
2
Enter the expression with arithmetic operator:a+b+c
temp=a+b
temp1=temp+c

lab1-16@lab1-16:~/Harshad$ ./a.out
Enter your choice	1:Assignment	2:Arithmetic	3:Relational	4:exit
3
Enter the expression with relational statement:
a
<=
b
100	if a<=b goto 103
101	 T:=0
102	 goto 104
103	 T:=1
lab1-16@lab1-16:~/Harshad$ 
*/
