/**
 * Proszę wyświellić na ekranie prostokąt mający 8 gwiazdek w wierszu i 4 takie
 * wiersze
 */

#include <iostream>
#include <string>

int main() {
    int wiersze, kolumny = 0;
    std::cout << "Podaj liczbę wierszy: " << std::endl;
    std::cin >> wiersze;
    std::cout << "Podaj liczbę kolumn: " << std::endl;
    std::cin >> kolumny;

    for (int i = 0; i < wiersze; i++) {
        for (int k = 0; k < kolumny; k++) {
            std::cout << "*";
        }
        std::cout << std::endl;
    }

    getchar();
    return 0;
}