/**
 * n to liczba naturalna podana przez użytkownika.
 * Oblicz sumę liczb parzystych od 1 do n.
 */

#include <stdio.h>

int main() {
    int max, suma_parzystych, suma_nieparzystych = 0;
    printf("Podaj górną granicę przedziału: ");
    scanf("%i", &max);

    // Suma sumy parzystych
    for (int i = 0; i <= max; i += 2) {
        suma_parzystych += i;
    }

    // Obliczanie sumy nieparzystych
    for (int i = 0; i <= max; i++) {
        if (i % 2 != 0) {
            suma_nieparzystych += i;
        }
    }

    float iloraz = suma_parzystych / suma_nieparzystych;

    printf("Suma liczb parzystych od 1 do %i to %i\n", max, suma_parzystych);
    printf("Suma liczba nieparzystych od 1 do %i to %i\n", max,
           suma_nieparzystych);
    printf("%i podzielone przez %i to %.2f\n", suma_parzystych,
           suma_nieparzystych, iloraz);

    getchar();
    return 0;
}