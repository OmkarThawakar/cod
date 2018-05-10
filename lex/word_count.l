
%{
	#include<stdio.h>
	int count=0;
%}
%%
['\t'] {count++;}

%%

int main(){
	yyin = fopen('myfile.txt','r');
	yyset_in(yyin);
	yylex();
	fclose(yyin);
	printf("No of words : %d",count);
	return 0;
	
}