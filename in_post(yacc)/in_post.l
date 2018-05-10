%{
#include"y.tab.h"
extern int yylval;
%}
%%
[0-9]+  {yylval=atoi(yytext); return NUM;}
\n      return 0;
.       return *yytext;
%%

int yywrap(){
    return 1;
}

/*
shell
yacc -d gram.y
flex gram.l
cc lex.yy.c y.tab.c
./a.out



output:
2+6*2-5/3
262*+53/-
*/