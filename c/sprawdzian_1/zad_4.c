/**
 * Zadanie 4 - programy w telewizji.
 */

#include <stdio.h>

int main() {
    int wiek;
    printf("Proszę podać wiek: ");
    scanf("%i", &wiek);

    if (wiek <= 0) {
        printf("Niewłaściwy wiek!\n");
        getchar();
        return 0;
    }

    if (wiek <= 11) {
        printf("Kategoria: dzieci do 11 lat\n");
    } else if (wiek >= 12 && wiek <= 16) {
        printf("Kategoria: młodzież od 12 lat\n");
    } else if (wiek >= 16) {
        printf("Kategoria: młodzież od 16 lat\n");
    }

    getchar();
    return 0;
}