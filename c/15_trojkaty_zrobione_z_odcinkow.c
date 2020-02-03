/**
 * Użytkownik podaje 3 dodatnie liczby rzeczywiste. Program wyświetla
 * następujące informacje (tak/nie):
 * a) Czy da się zbudowac z tych odcinków trójkat równoramienny?
 * b) Czy da się zbudowac z tych odcinków trójkąt prostokątny?
 */

#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

int main() {
    float a, b, c;
    bool jest_rownoramienny, jest_prostokatny;

    printf("Podaj pierwszy bok: ");
    scanf("%f", &a);

    printf("Podaj drugi bok: ");
    scanf("%f", &b);

    printf("Podaj trzeci bok: ");
    scanf("%f", &c);

    if (a <= 0 || b <= 0 || c <= 0) {
        printf("Każdy bok musi być liczbą dodatnią!\n");
        getchar();
        return 0;
    }

    if (a >= b && a >= c) {
        // a jest najdłuższym bokiem
        if (b + c <= a) {
            printf("To nie jest trójkąt!\n");
            getchar();
            return 0;
        }

        if (b == c) {
            jest_rownoramienny = true;
        }

        if ((b * b + c * c) == a * a) {
            jest_prostokatny = true;
        }
    }

    else if (b >= a && b >= c) {
        // b jest najdłuższym bokiem

        if (a + c <= b) {
            printf("To nie jest trójkąt!\n");
            getchar();
            return 0;
        }

        if (a == c) {
            jest_rownoramienny = true;
        }

        if ((a * a + c * c) == b * b) {
            jest_prostokatny = true;
        }
    }

    else if (c >= a && c >= b) {
        // c jest najdłuższym bokiem
        if (a + b <= c) {
            printf("To nie jest trójkąt!\n");
            getchar();
            return 0;
        }

        if (a == b) {
            jest_rownoramienny = true;
        }

        if ((a * a + b * b) == c * c) {
            jest_prostokatny = true;
        }
    }

    if (jest_prostokatny) {
        printf("Jest to trójkąt prostokątny\n");
    } else {
        printf("Nie jest to trójkąt prostokątny\n");
    }

    if (jest_rownoramienny) {
        printf("Jest to trójkąt równoramienny\n");
    } else {
        printf("Nie jest to trójkąt równoramienny\n");
    }

    getchar();
    return 0;
}