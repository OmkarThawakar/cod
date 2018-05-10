
%{
	#include<stdio.h>
	int count=0;
%}
%%
[A-Z] { printf("Echo : %s \n",yytext);
		 count++;
		}
. ;
%%

int main(){
	yylex();
	printf("Capital Character are : %d \n",count);
	return 0;
}