/*
Aim-: Write a C or C++ program for code generation.
*/
/* ****** PROGRAM ****** */
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<ctype.h>
char op[10],arg1[10],arg2[10],result[10];
void main(){
  	FILE *fp1,*fp2;
  	fp1=fopen("input.txt","r");
  	fp2=fopen("output.txt","w");
  	while(!feof(fp1)){
		fscanf(fp1,"%s%s%s%s",op,arg1,arg2,result);
    	if(strcmp(op,"+")==0){
      		fprintf(fp2,"\nMOV R0,%s",arg1);
      		fprintf(fp2,"\nADD R0,%s",arg2);
      		fprintf(fp2,"\nMOV %s,R0",result);
    	}
     	if(strcmp(op,"*")==0){
      		fprintf(fp2,"\nMOV R0,%s",arg1);
      		fprintf(fp2,"\nMUL R0,%s",arg2);
      		fprintf(fp2,"\nMOV %s,R0",result);
    	}
    	if(strcmp(op,"-")==0){
      		fprintf(fp2,"\nMOV R0,%s",arg1);
      		fprintf(fp2,"\nSUB R0,%s",arg2);
      		fprintf(fp2,"\nMOV %s,R0",result);
    	}
    	if(strcmp(op,"/")==0){
      		fprintf(fp2,"\nMOV R0,%s",arg1);
      		fprintf(fp2,"\nDIV R0,%s",arg2);
      		fprintf(fp2,"\nMOV %s,R0",result);
    	}
    	if(strcmp(op,"=")==0){
      		fprintf(fp2,"\nMOV R0,%s",arg1);
      		fprintf(fp2,"\nMOV %s,R0",result);
    	}
	}
    fclose(fp1);
    fclose(fp2);
}
/* ****** OUTPUT ******
lab1-16@lab1-16:~/Harshad$ gcc P11.c
lab1-16@lab1-16:~/Harshad$ ./a.out
lab1-16@lab1-16:~/Harshad$ 
*/

/*input.txt
+ a b t1
* c d t2
- t1 t2 t
= t ? x
*/

/*output.txt
MOV R0,a
ADD R0,b
MOV t1,R0
MOV R0,c
MUL R0,d
MOV t2,R0
MOV R0,t1
SUB R0,t2
MOV t,R0
MOV R0,t
MOV x,R0
MOV R0,t
MOV x,R0
*/
