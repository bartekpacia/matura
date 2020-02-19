/**
 * Napisz porgram, który wyświetla czy dana liczba jest liczbą pierwszą.
 */
#include <math.h>
#include <iostream>
#include <string>

int main() {
    int liczba;

    std::cout << "Podaj liczbę naturalną: " << std::endl;
    std::cin >> liczba;

    if (liczba <= 0 || liczba > INT_MAX) {
        std::cout << "Niewłaściwa liczba" << std::endl;
        getchar();
        return 0;
    }

    bool pierwsza = true;
    for (int i = 2; i < liczba; i++) {
        if (liczba % i == 0) {
            pierwsza = false;
        }
    }

    if (pierwsza) {
        std::cout << "Jest liczbą pierwszą" << std::endl;
    } else {
        std::cout << "Nie jest liczbą pierwsza" << std::endl;
    }

    getchar();
    return 0;
}
