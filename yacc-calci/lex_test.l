/*
aim : design yacc program for simple calculator

name : Omkar Thawakar
Reg No : 2015bcs0003 
Batch : A-01
*/

%{
	#include<stdio.h>
	#include<math.h>
	#include "y.tab.h"

	extern int yylval;

%}

%%

[0-9]+ { yylval = atoi(yytext); return NUMBER;}
[+] { return '+' ;}
[-] { return '-' ;}
[*] { return '*' ;}
[/] { return '/' ;}
[\n] { return 0;}
. { return yytext[0];}

%%
