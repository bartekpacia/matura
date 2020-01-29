/**
 * Użytownik podaje liczbę naturalną.
 * Program wyświetla czy jest jedno, dwu, trzy, czy czterocyfrowa.
 */

#include <stdio.h>

int main() {
    int number;
    printf("Podaj liczbę: ");
    scanf("%i", &number);

    if (number / 10 < 1) {
        printf("jednocyfrowa liczba");
    } else if (number / 10 < 10) {
        printf("dwucyfrowa");
    } else if (number / 10 < 100) {
        printf("trzycyfrowa");
    } else if (number / 10 < 1000) {
        printf("czterocyfrowa");
    }

    getchar();
    return 0;
}