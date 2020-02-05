/**
 * Użytkownik podaje znak. Program wypisuje, czy jest to litera duża, czy jest
 * to litera mała, czy jest to inny znak.
 */
#include <stdio.h>

int main() {
    char znak;
    printf("Podaj znak: ");
    scanf("%c", &znak);

    if (znak >= 'A' && znak <= 'Z') {
        printf("Duża litera\n");
    } else if (znak >= 'a' && znak <= 'z') {
        printf("Mała litera\n");
    } else if (znak >= '0' && znak <= '9') {
        printf("Liczba\n");
    }

    else {
        printf("Inny znak\n");
    }

    getchar();
    return 0;
}