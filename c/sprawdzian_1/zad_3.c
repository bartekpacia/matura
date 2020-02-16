/**
 * Zadanie 3 – temperatura ciała.
 */

#include <stdio.h>

int main() {
    float temperatura = 0;

    printf("Podaj temperaturę ciała: ");
    scanf("%f", &temperatura);

    if (temperatura < 36.5) {
        printf("zbyt niska temperatura ciała\n");
    }

    if (temperatura >= 36.5 && temperatura <= 36.9) {
        printf("normalna temperatura ciałą\n");
    }

    if (temperatura > 36.9 && temperatura < 37.5) {
        printf("stan podgorączkowy\n");
    }

    if (temperatura >= 37.5 && temperatura < 40) {
        printf("gorączka\n");
    }

    if (temperatura >= 40) {
        printf("Bardzo wysoka gorączka. Koniecznie udaj się do lekarza\n");
    }

    getchar();
    return 0;
}