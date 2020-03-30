
/**
 * Zadanie 22 z książki (w przyszłości dodam tu treść)
 */

#include <iostream>

int main() {
    int liczba_wierszy = 0;

    std::cout << "Podaj liczbę: ";
    std::cin >> liczba_wierszy;

    if (liczba_wierszy <= 0) {
        std::cout << "Nieprawidłowa liczba wierszy!" << std::endl;
        return 0;
    }

    for (int i = 1; i <= liczba_wierszy; i++) {
        for (int j = 1; j <= i; j++) {
            std::cout << i;
        }

        std::cout << std::endl;
    }

    return 0;
}
