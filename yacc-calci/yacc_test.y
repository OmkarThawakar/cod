
/*
aim : design yacc program for simple calculator

name : Omkar Thawakar
Reg No : 2015bcs0003 
Batch : A-01

*/

%token NUMBER 
%left '-' '+'
%right '*' '/'

%%

start : expr { printf("Answer : %d ",$$); }
;
expr : expr'+'expr {$$=$1+$3;}
	   | expr'-'expr {$$=$1-$3;}
	   | expr'*'expr {$$=$1*$3;}
	   | '('expr')' {$$=$2;}
	   | NUMBER {$$=$1;}
	   | expr'/'expr {if($3==0) {yyerror("error");}	 else {$$=$1/$3;} }
;

%%

int yyerror(char *args){
	printf("Invalid Operation!!\n");
	exit(0);
}

main(){
	printf("Enter Number :");
	yyparse();
}
