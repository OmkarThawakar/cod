/*
aim : implement a YACC program which recognise 
valid variable or identifier with letter or "_" 
followed by any number of letter or digits.

name : Omkar Thawakar
Reg No : 2015bcs0003 
Batch : A-01

*/

%{
	#include<stdio.h>
	#include "y.tab.h"
%}

%%

[a-zA-Z] { return LETTER ;}
[0-9] { return DIGIT ;}
_ { return UNDSCORE ;}
[\\n] { return NEWLINE;}
. { return yytext[0];}

%%