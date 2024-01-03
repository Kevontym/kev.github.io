#include <stdio.h>
#include <stdlib.h>

int main() {

    // const int a = 10;
    // printf("%d\n", a);

    // a = 20;
    // printf("%d\n", a);

    // const float PI = 3.14159265;
    // const char NEWLINE = '\n';
    
    // printf("My favorite number is %.5f%c", PI, NEWLINE);
    
    // printf("%s", "HelloWorld!\n");

    // char mystring[10] = "Hello";
    // printf("%s\n", mystring);

    // int a = (int) 'A';
    // printf("%d\n", 'a');

    // char b = (char) 66;
    // printf("%c\n", b);

    // // char c = (char) 24.687;
    // // printf("%c\n", b)

    // float f = (float) 10;
    

    // char mystring[10] = "1788.912";
    // float f = atof(mystring);
    // printf("%.3f\n", f);

    char mystring[10];
    int i = 20;
    sprintf(mystring, "%d", i);
    printf("%s", mystring);

    return 0;
}