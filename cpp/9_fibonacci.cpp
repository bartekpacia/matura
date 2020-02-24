/**
 * Napisz program, który oblicza ciąg Fibonacciego.
 * 0, 1, 1, 2, 3, 5, 8, 13
 * 0 + 1 = 1
 * 1 + 1 = 2
 * 1 + 2 = 3
 * 2 + 3 = 5
 * 3 + 5 = 8
 * 5 + 8 = 13
 */

#include <iostream>

int main() {
    int max = 0;
    int f0 = 0;
    int f1 = 1;

    std::cout << "Podaj max liczbę: ";
    std::cin >> max;

    for (int i = 0; i <= max; ++i) {
        int liczba_ciagu = f1 + f0;
        f0 = f1;
        f1 = liczba_ciagu;

        std::cout << i + 1 << " liczba ciągu: " << liczba_ciagu << std::endl;
    }

    return 0;
}
