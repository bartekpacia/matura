/**
 * n to liczba naturalna podana przez użytkownika.
 * Oblicz sumę liczb parzystych od 1 do n.
 */

#include <stdio.h>

int main() {
    int max, suma = 0;
    printf("Podaj górną granicę przedziału: ");
    scanf("%i", &max);

    for (int i = 0; i <= max; i += 2) {
        suma += i;
    }

    printf("Suma liczba od 1 do %i to %i\n", max, suma);

    getchar();
    return 0;
}