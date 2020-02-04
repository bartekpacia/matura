/**
 * Użytkownik podaje dodatnią liczbę całkowitą z zakresu <1600; 2500>
 * oznaczającą rok. Program wyświetla czy podany rok jest przestępny.
 *
 * pro tip:
 * Podzielne przez 100, niepodzielne przez 400 nie jest rokiem przestepnym.
 * Kazdy inny przez 4 przestepny
 */
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

int main() {
    int rok;
    bool przestepny;

    printf("Podaj rok: ");
    scanf("%i", &rok);

    if (!(rok >= 1600 && rok <= 2500)) {
        printf("Rok %i nie mieści się w przedziale od 1600 do 2500\n", rok);
        getchar();
        return 0;
    }

    if (rok % 100 == 0 && rok % 400 != 0) {
        przestepny = false;
    } else if (rok % 4 == 0) {
        przestepny = true;
    } else {
        przestepny = false;
    }

    if (przestepny) {
        printf("Rok %i jest przestępny\n", rok);
    } else {
        printf("Rok %i NIE jest przestępny\n", rok);
    }

    getchar();
    return 0;
}