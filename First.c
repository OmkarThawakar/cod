/*
Reg. No.-: 2015BCS034
Roll No.-: B19
Aim-: Write a C program to calculate FIRST of a given grammar.
*/
/* ****** PROGRAM ****** */
#include<stdio.h>
#include<ctype.h>
char ch,c;
int i,n;
char aa[10][10];
char first[10];
void result(char ch){
    int j=0;
    for(i=1;i<=n;i++){
        if(ch==aa[i][j]){
	    if(isupper(aa[i][2])){
		result(aa[i][2]);
	    } else {
		printf("The first of %c is {%c}\n",aa[i][0],aa[i][2]);
	    }
        }
    }
}
void main(){
    printf("Number of production:\n");
    scanf("%d",&n);
    for(i=1;i<=n;i++){ 
	printf("Enter the production %d\n",i);
	scanf("%s",aa[i]);
    }
    do{
	printf("Find the first of:\n");
	scanf("%s",&ch);
	result(ch);
	printf("Do you wish to continue (y/n)\n");
	scanf("%s",&c);
    }while(c=='y' || c=='Y');
}
/* ****** OUTPUT ******
lab-1pc17@lab-1pc17:~/Desktop$ gcc First.c
lab-1pc17@lab-1pc17:~/Desktop$ ./a.out
Number of production:
8
Enter the production 1
E=TD
Enter the production 2
D=+TD
Enter the production 3
D=$
Enter the production 4
T=FS
Enter the production 5
S=+FS
Enter the production 6
S=$
Enter the production 7
F=(E)
Enter the production 8
F=a
Find the first of:
E
The first of F is {(}
The first of F is {a}
do you wish to continue y/n
y
Find the first of:
S
Fhe first of S is {+}
Fhe first of S is {$}
Do you wish to continue y/n
y
Find the first of:
T
The first of F is {(}
The first of F is {a}
Do you wish to continue y/n
*/
