/**
 * Zadanie 2 - stawka godzinowa.
 **/
/**
 * Użytkownik podaje 2 liczby rzeczywiste. Program wyświetla ich iloczyn.
 */

#include <stdio.h>

int main() {
    int ilosc_godzin = 0;
    int stawka_godzinowa = 0;

    printf("Podaj ilość godzin: ");
    scanf("%i", &ilosc_godzin);

    printf("Podaj stawkę godzinową: ");
    scanf("%i", &stawka_godzinowa);

    if (ilosc_godzin < 0) {
        printf("Zła ilość godzin!\n");
        getchar();
        return 0;
    }

    if (stawka_godzinowa <= 0) {
        printf("Niewłaściwe dane. To praca, nie wolontariat!\n");
        getchar();
        return 0;
    }

    float wyplata = 0;

    if (ilosc_godzin > 40) {
        // Mamy nadgodziny
        int nadgodziny = ilosc_godzin - 40;
        printf("nadgodziny: %i\n", nadgodziny);

        float wyplata_za_baze = 40 * stawka_godzinowa;
        float wyplata_za_nadgodziny = nadgodziny * (stawka_godzinowa * 1.5);
        wyplata = wyplata_za_baze + wyplata_za_nadgodziny;

    } else {
        wyplata = stawka_godzinowa * ilosc_godzin;
    }

    printf("Wypłata: %.2f\n", wyplata);

    getchar();
    return 0;
}