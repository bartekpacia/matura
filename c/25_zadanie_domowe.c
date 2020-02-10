/**
 * Oblicz sumę następującego ciągu: 1/1 + 1/2 + 1/3 + 1/4 + 1/5 + 1/6 + 1/n
 * n to liczba naturalna podana przez użytkownika
 */

#include <stdio.h>

int main() {
    int max;
    float suma = 0;
    printf("Podaj górną granicę przedziału: ");
    scanf("%i", &max);

    for (int n = 1; n <= max; n++) {
        float nowy_ulamek = 1 / (float)n;
        suma += nowy_ulamek;
    }

    printf("Suma liczba od 1 do 1 / %i to %f\n", max, suma);

    getchar();
    return 0;
}