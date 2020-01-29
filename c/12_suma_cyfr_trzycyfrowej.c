/**
 * Użytkownik podaje dodatnią całkowitą liczbę trzycyfrową. Program wyświetla
 * sumę jej cyfr.
 */

#include <stdio.h>

int main() {
    int liczba;

    printf("Podaj liczbę trzycyfrową: ");
    scanf("%i", &liczba);

    if (liczba < 0) {
        printf("Liczba nie może być mniejsza niż zero!\n");
    } else {
        int liczba_niezmieniona = liczba;

        int suma = 0;
        while (liczba != 0) {
            suma += liczba % 10;
            liczba /= 10;
        }

        printf("Suma cyfr w liczbie %i wynosi %i\n", liczba_niezmieniona, suma);
    }

    getchar();
    return 0;
}