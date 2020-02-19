/**
 * Napisz porgram, który dla podanej liczby naturalnej n wyświetli wszystkie
 * jej podzielniki.
 */
#include <math.h>
#include <iostream>

int main() {
    int liczba;

    std::cout << "Podaj liczbę naturalną: " << std::endl;
    std::cin >> liczba;

    if (liczba <= 0 || liczba > INT_MAX) {
        std::cout << "Niewłaściwa liczba" << std::endl;
        getchar();
        return 0;
    }

    for (int i = 1; i <= (liczba / 2); i++) {
        if (liczba % i == 0) {
            std::cout << "Liczba " << i << " jest podzielnikiem liczby "
                      << liczba << std::endl;
        }
    }

    getchar();
    return 0;
}
