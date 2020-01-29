/**
 * Użytkownik podaje liczbę naturalną. Pprogram wyświetla informację, czy liczba
 * jest:
 * 1. parzysta / nieparzysta.
 * 2. podzielna przez 5
 */

#include <math.h>
#include <stdio.h>

/**
 * W tym momencie widać, że Pani Stacha nie powiedziała nam pełni prawdy.
 * W C istnieje bool, tylko trzeba go sobie zaimportować.
 */
#include <stdbool.h>

int main() {
    int number = 0;
    bool divisible = false;
    printf("Podaj liczbę: ");
    scanf("%i", &number);

    if (number % 2 == 0) {
        printf("Liczba %i jest parzysta \n", number);
        divisible = true;
    }

    if (number % 5 == 0) {
        printf("Liczba %i jest podzielna przez 5 \n", number);
        divisible = true;
    }

    if (!divisible) {
        printf("Liczba %i nie jest ani parzysta ani podzielna przez 5 \n",
               number);
    }

    getchar();

    return 0;
}