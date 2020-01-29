/**
 * Użytkownik podaje 2 liczby rzeczywiste. Program wyświetla ich iloczyn.
 */

#include <stdio.h>

int main() {
    float a;
    float b;
    printf("Wprowadź pierwszą liczbę: ");
    scanf("%f", &a);
    printf("Wprowadź pierwszą liczbę: ");
    scanf("%f", &b);

    float suma = a * b;
    printf("Iloczyn %f i %f wynosi: %f\n", a, b, suma);
    printf("Iloczyn %.2f i %.2f wynosi: %.2f\n", a, b, suma);

    getchar();
    return 0;
}