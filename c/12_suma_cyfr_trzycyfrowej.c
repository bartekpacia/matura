/**
 * Użytkownik podaje dodatnią całkowitą liczbę trzycyfrową. Program wyświetla
 * sumę jej cyfr.
 */

#include <stdio.h>

int main() {
    int liczba = 0;

    printf("Podaj liczbę trzycyfrową: ");
    scanf("%i", &liczba);

    if (liczba < 0) {
        printf("Liczba nie może być mniejsza niż zero!\n");
        getchar();
        return 0;
    }

    int suma = 0;

    while (liczba != 0) {
        int reszta = liczba % 10;
        suma = suma + reszta;
        liczba = liczba / 10;
    }

    printf("Suma cyfr tej liczby wynosi %i\n", suma);

    getchar();
    return 0;
}

/**
 * Dla Michała Bartoszka<3
 *****Przykład działania programu dla liczby 69:
 *
 * 1 iteracja
 * reszta = 69 % 10 = 9
 * suma = 0 + 9 = 9
 * liczba = 69 / 10 = 6
 *
 * 2 iteracja
 * reszta = 6 % 10 = 6
 * suma = 9 + 6 = 15
 * liczba = 6 / 10 = 0
 *
 * liczba = 0 -> koniec pętli
 *
 *
 ***** Przykład działania programu dla liczby 125:
 *
 * 1 iteracja
 * reszta = 125 % 10 = 5
 * suma = 0 + 5 = 5
 * liczba = 125 / 10 = 12
 *
 * 2 iteracja
 * reszta = 12 % 10 = 2
 * suma = 5 + 2 = 7
 * liczba = 12 / 10 = 1
 *
 * 3 iteracja
 * reszta = 1 % 10 = 1
 * suma = 7 + 1 = 8
 * liczba = 1 / 10 = 0
 *
 * liczba = 0 -> koniec pętli
 **/