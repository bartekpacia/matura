/**
 * Użytkownik podaje liczbę rzeczywistą będąca promieniem koła. Program
 * wyświetla obwód i pole koła z tym promieniem.
 */

#include <math.h>
#include <stdio.h>

int main() {
    float radius = 0;
    printf("Podaj promień koła: ");
    scanf("%f", &radius);

    if (radius <= 0) {
        printf("Promień koła < 0 \n");
        getchar();
        return 1;
    }

    float area = M_PI * radius * radius;
    float circumference = 2 * M_PI * radius;

    printf("Pole: %f \n", area);
    printf("Obwód: %f \n", circumference);

    getchar();

    return 0;
}