/**
 * Użytkownik podaje 3 liczby rzeczywiste. Program wyświetla największą z nich.
 */

#include <stdio.h>

int main() {
    float liczba1, liczba2, liczba3, najwieksza;

    printf("Podaj pierwszą liczbę: ");
    scanf("%f", &liczba1);

    printf("Podaj drugą liczbę: ");
    scanf("%f", &liczba2);

    printf("Podaj trzecią liczbę: ");
    scanf("%f", &liczba3);

    if (liczba1 > liczba2 && liczba1 > liczba3) {
        najwieksza = liczba1;
    }

    if (liczba2 > liczba1 && liczba2 > liczba3) {
        najwieksza = liczba2;
    }

    if (liczba3 > liczba1 && liczba3 > liczba2) {
        najwieksza = liczba3;
    }

    printf("Najwieksza liczba: %f \n", najwieksza);
    getchar();

    return 0;
}