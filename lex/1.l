%{
	#include<stdio.h>
	int count=0;
%}
%%
.*{printf("character found ");}
%%

int main(){
	yylex();
	printf("Character are : %d",count);
	return 0;
}