/**
 * Wypełnić tablicę losowymi liczbami i obliczyć sumę liczb podzielnych przez 6
 * w tej tablicy.
 */
#include <cstdlib>
#include <ctime>
#include <iostream>

int main() {
    int rozmiar = 5;
    int tabela[rozmiar][rozmiar];

    srand(time(NULL));

    // Zapełnianie tabeli losowymi liczbami od 0 to 9
    for (int i = 0; i < rozmiar; i++) {
        for (int j = 0; j < rozmiar; j++) {
            tabela[i][j] = rand() % 10;
        }
    }

    // Wyświetlenie tabeli
    for (int i = 0; i < rozmiar; i++) {
        for (int j = 0; j < rozmiar; j++) {
            std::cout << tabela[i][j] << " ";
        }

        std::cout << std::endl;
    }

    // Przykład dostępu do elementu matrycy.
    std::cout << "tab[2][1] = " << tabela[2][1] << std::endl;

    return 0;
}
