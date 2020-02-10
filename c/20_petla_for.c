/**
 * Program wyświetla liczby naturalne z przedziału 1..n;
 */

#include <stdio.h>

// Wykonywanie każdego programu zaczyna się od funkcji nazwanej main.
int main() {
    int max;
    printf("Podaj górną granicę przedziału, który chcesz wyświetlić: ");
    scanf("%i", &max);

    if (max <= 0) {
        printf("Liczba musi być większa od zera\n");
        getchar();
        return 0;
    }

    for (int current = 0; current <= max; current++) {
        printf("%i\n", current);
    }

    getchar();
    return 0;
}