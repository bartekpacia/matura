/**
 * Użytkownik podaje 3 dodatnie liczby rzeczywiste. Program wyświetla
 * następujące informacje (tak/nie):
 * a) Czy da się zbudowac z tych odcinków trójkat równoramienny?
 * b) Czy da się zbudowac z tych odcinków trójkąt prostokątny?
 */

#include <stdio.h>
#include <stdlib.h>

int main() {
    float a, b, c;

    printf("Podaj pierwszy bok: ");
    scanf("%f", &a);

    printf("Podaj drugi bok: ");
    scanf("%f", &b);

    printf("Podaj trzeci bok: ");
    scanf("%f", &c);

    if (a <= 0 || b <= 0 || c <= 0) {
        printf("Każdy bok musi być liczbą dodatnią!");
        getchar();
        return 0;
    }

    
    getchar();
    return 0;
}