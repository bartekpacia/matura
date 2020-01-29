/**
 * Użytkownik podaje dwie całkowite liczby dodatnie będące
 * długosciami boków prostokatą. Program wyświetla pole powierzchni największego
 * kwadratu mieszczącego sie w prostokącie o wczytanych bokach.
 */
#include <stdio.h>
#include <stdlib.h>

int main() {
    int a, b, pole_prostokata;
    printf("Podaj dwie całkowite liczby dodatnie: ");
    scanf("%i", &a);
    scanf("%i", &b);

    if (a >= b) {
        pole_prostokata = b * b;
    } else if (b > a) {
        pole_prostokata = a * a;
    }

    printf(
        "Pole największego kwadratu mieszczącego sie w prostokącie o bokach %i "
        "x %i wynosi %i\n",
        a, b, pole_prostokata);

    getchar();
    return 0;
}