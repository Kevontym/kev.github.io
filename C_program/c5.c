#include <stdio.h>


int main() {

    int a = 10;
    int b = 20;

    int choice;
    printf("Enter a number: ");
    scanf("%d", &choice);

    if (choice < 100) {
        printf("Your input is less than 100\n");
        if (choice < 50) {
        printf("Your input is also less than fifty\n");
        } 
        else if (choice < 200) {
            printf("Your input is between 100 and 200\n");
    }
    } else { 
        printf("Your input is not less than a hundred\n");
    }

    switch {
        case 100;
        printf("You have one hundred");
        break;

        case 50;
        printf("You have 50");
        break;

        case 10;
        printf("you have 10");
    }

    return 0;
}