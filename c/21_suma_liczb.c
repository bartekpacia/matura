#include <stdio.h>
int main() {
    int max, suma = 0;
    printf("Podaj górną granicę przedziału: ");
    scanf("%i", &max);
    for (int i = 0; i <= max; i++) {
        suma += i;
    }
    printf("Suma liczba od 1 do%i to%i\n", max, suma);
    getchar();
    return 0;
}