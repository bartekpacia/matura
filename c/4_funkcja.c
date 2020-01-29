/**
 * Użytkownik podaje liczbę rzeczywistą x.
 * Program wyświetla wartośc funkcji f dla x podanego przez użytkownika
 *
 *  f(x) = (3x -5) / 4x
 */

#include <math.h>
#include <stdio.h>

int main() {
    float x = 0;
    printf("Podaj x: ");
    scanf("%f", &x);

    float y = (3 * x - 5) / 4 * x;

    printf("(3 * %.2f - 5) / 4 * %.2f = %.2f \n", x, x, y);

    getchar();

    return 0;
}