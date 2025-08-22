// source code -> compiler -> machine code
//GUI - Graphical User Interface
//CLI - Command Line Interface  
#include<stdio.h> //any file that ends with .h called an header files
// and all the header files always came with an programming language it
//is a feature of that language not independent of this
//without header file you do not access of libraries
#include<string.h>


int main(void){
    char answer[50];
    // scanf("%s",&answer);
    fgets(answer,50,stdin);
    printf("%s",answer);
    printf("Hello, world\n");
}

//format strings 
// %s %c %f %i %li  

/* bool char double float int long string 
get_char get_double get_float get_int get_long get_string*/


//One is a GUI and one is a CUI
//What is the difference between hello and hello.c?
//hello.c is literally the my srccode file 
//on the other hand the hello file is created by compiler for me 
//what if we don't type ./hello and type hello then there is any mistake
//any programme rewrite there is a default things ls/mkdir/rm/rmdir
//use this
//what's look wrong to my eye now? % sign automatically add there

//arguments -> function -> sideEffects
// \n -> new line \r -> not new line just the beginning of the line 
// \" \' \\ ... all are escape characters
// \ is a special character which returns new line carriage return or backslashes
