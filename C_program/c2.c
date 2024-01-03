#include <stdio.h>
#include <limits.h>

int main() {

    int a = 10;
    int b = 20;
    int c = 30;

    printf("%d + %d = %d\n", a, b, c);
    printf("%ld\n", sizeof(a));

    short d = 500;
    printf("%d\n", d);
    printf("%ld\n", sizeof(d));

    printf("INT MAX VALUE: %d\n", INT_MAX);
    printf("INT MIN VALUE: %d\n", INT_MIN);

    printf("SHORT MAX VALUE: %d\n", SHRT_MAX);
    printf("SHORT MIN VALUE: %d\n", SHRT_MIN);

    long e = 2233243494;
    long long f = 235125533;
    printf("%ld\n", e);
    printf("%ld\n", e);
    printf("SIZE LONG: %ld\n", sizeof(e));
    printf("SIZE LONG LONG: %ld\n", sizeof(f));


    printf("Long MAX VALUE: %ld\n", LONG_MAX);
    printf("Long Long MIN VALUE: %lld\n", LLONG_MAX);

    unsigned long int g = 2147443646483648;
    printf("%lu\n", g);
    printf("UNSIGNED LONG LONG MAX: %llu\n", ULLONG_MAX);

    return 0;
}