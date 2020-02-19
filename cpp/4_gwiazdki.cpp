/**
 * Proszę wyświellić na ekranie prostokąt mający 8 gwiazdek w wierszu i 4 takie
 * wiersze
 */

#include <iostream>

int main() {
    int wiersze, kolumny = 0;
    std::cout << "Podaj liczbę wierszy: " << std::endl;
    std::cin >> wiersze;
    std::cout << "Podaj liczbę kolumn: " << std::endl;
    std::cin >> kolumny;

    if (!(wiersze > 0 && kolumny > 0)) {
        std::cout << "Podane niewłaściwe dane" << std::endl;
        getchar();
        return 0;
    }

    for (int i = 0; i < wiersze; i++) {
        for (int k = 0; k < kolumny; k++) {
            std::cout << "*";
        }
        std::cout << std::endl;
    }

    getchar();
    return 0;
}