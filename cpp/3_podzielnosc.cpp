#include <iostream>

/**
 * Wszystkie liczby dodatnie mniejsze od k podzielne przez n.
 * k i n to liczby naturalne podawane przez użytkownika.
 */

int main() {
    int k, n = 0;
    std::cout << "Podaj k: " << std::endl;
    std::cin >> k;
    std::cout << "Podaj n: " << std::endl;
    std::cin >> n;

    if (k < 1 || n < 1) {
        std::cout << "Podane niewłaściwe dane" << std::endl;
        getchar();
        return 0;
    }

    if (k < n) {
        std::cout << "Brak dzielników liczby " << n << " w przedziale <1; " << k
                  << ">" << std::endl;
    }

    for (int i = 1; i <= k; i++) {
        if (i % n == 0) {
            std::cout << "Znaleziono liczbę " << i << " podzielną przez " << n
                      << std::endl;
        }
    }

    getchar();
    return 0;
}