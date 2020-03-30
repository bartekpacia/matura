
/**
 * Napisz program, który wypisze wszystkie liczby całkowite dodatnie (oddzielone
 * spacją) mniejsze od k (k wprowadzone z klawiatury), które mają dokładnie trzy
 * dzielniki. W przypadku braku takich liczb program powinien wypisać słowo
 * „BRAK".
 */

#include <iostream>

int main() {
    int k = 0;

    std::cout << "Podaj liczbę: ";
    std::cin >> k;

    int liczba_podzielnikow = 0;
    for (int i = 1; i < k; i++) {
        int podzielniki = 0;
        for (int j = 1; j < k; j++) {
            if (i % j == 0) {
                podzielniki += 1;
            }
        }

        if (podzielniki == 3) {
            std::cout << i << " ";
            liczba_podzielnikow++;
        }
    }

    std::cout << std::endl;

    if (liczba_podzielnikow < 1) {
        std::cout << "BRAK" << std::endl;
    }

    return 0;
}
