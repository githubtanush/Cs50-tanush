#include<stdio.h>
// #include<cs50.h>
int main(){
    string name = get_string("What's your name? ");
    printf("hello,%s\n",name);
    return 0;
}
//clang -o hello hello.c -lcs50 => lcs = library cs
// ./hello