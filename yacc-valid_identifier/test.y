/*
aim : implement a YACC program which recognise 
valid variable or identifier with letter or "_" 
followed by any number of letter or digits.

name : Omkar Thawakar
Reg No : 2015bcs0003 
Batch : A-01

*/

/*
context free grammer

S -> LX|USX
X -> L|D|US
L -> LETTER
D -> DIGIT
US -> UNDSCORE

{{another way!!}}
S -> var NL
var -> LETTER alpha | UND alpha
alpha -> LETTER|DIGIT|UNDSCORE|LETTER alpha|DIGIT alpha|UNDSCORE alpha
*/

%{
	#include<stdio.h>
	#include<stdlib.h>
%}

%token LETTER DIGIT UNDSCORE NEWLINE 


%%

S : var { printf("Valid Identifier!!\n"); }
;
var : LETTER alpha {} | UNDSCORE alpha {}
;
alpha : LETTER {} |
		DIGIT {} |
		UNDSCORE {} |
		LETTER alpha {} |
		DIGIT alpha {} |
		UNDSCORE alpha {}  
;

%%

int yyerror(char *args){
	printf("Invalid Tokens!!\n");
	exit(0);
}

main(){
	printf("Enter your String : \n");
	yyparse();
}