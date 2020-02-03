/**
 * Użytkownik podaje dwie całkowite liczby dodatnie. Liczby te oznaczają
 * odpowiednio długosc drogi oraz długość kroku. Program wyświetla minimalną
 * liczbę kroków potrzebną do pokonania odległosci większej niz długość drogi.
 */
#include <stdio.h>
#include <stdlib.h>

int main() {
    int dlugosc_kroku;
    int dlugosc_drogi;
    int liczba_krokow;

    printf("Podaj długość drogi: ");
    scanf("%i", &dlugosc_drogi);

    printf("Podaj długość kroku: ");
    scanf("%i", &dlugosc_kroku);

    liczba_krokow = dlugosc_drogi / dlugosc_kroku + 1;
    printf("Liczba krokow potrzebnych do pokonania drogi %i to %i\n",
           dlugosc_drogi, liczba_krokow);

    getchar();
    return 0;
}