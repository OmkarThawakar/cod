
%{
	#include<stdio.h>
	int count=0;
%}
%%
[+]?(91|0)?[-]?[7-9][0-9]{2} { printf("Valid \n");
		 
		}
.* {printf("Invalid\n");}
%%

int main(){
	yylex();
	return 0;
}