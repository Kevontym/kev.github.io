#include <stdio.h>
#include <stdlib.h>

int main() {
    
    double pennies = .01;
    double nickels = .05;
    double dimes = .10;
    double quarters = .25;

    double one_dollar = 1.00;
    double five_dollar = 5.00;
    double ten_dollars = 10.00; 
    double twenty_dollars = 20.00;
    double fifty_dollars = 50.00;
    double one_hundred = 100.00;

    

    //Ask user for Cash
    double deposit;
    printf("Enter your cash in dispenser: ");
    // use "%lf" for scanning a doub value
    if (scanf("%lf", &deposit) != 1) {
    printf("Invalid tokens. Please try again");
    return 1;
    }


    if ((int) deposit % 2 == 0) {
        printf("Your money will return even!\n");
    } else { 
        printf("Here is your change thank you!\n");
    }

    

    return 0;

}
