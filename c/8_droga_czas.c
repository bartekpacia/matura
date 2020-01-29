/**
 * Użytkownik podaje liczbę rzeczywistą będącą drogą. Program wyświetla,
 * ile czasu zajmie pokonanie tej drogi z prędkością 90 km/h/
 */

#include <stdio.h>

const float v = 25;  // 25 m/s = 90 km / h

int main() {
    float s;
    printf("Podaj drogę w m: \n");
    scanf("%f", &s);

    if (s <= 0) {
        printf("Droga nie może być mniejsza od 0!");
        return 1;
    }

    float t = s / v;

    printf("Drogę %.2f metrów z prędkością %.2f m/s pokonasz w %.2f sekund", s,
           v, t);

    getchar();
    return 0;
}