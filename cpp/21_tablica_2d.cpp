/**
 * Wypełnić tablicę losowymi liczbami i obliczyć sumę liczb podzielnych przez 6
 * w tej tablicy.
 */
#include <iostream>

int main() {
    int rozmiar = 5;
    int tabela[rozmiar][rozmiar];

    srand(time(NULL));

    for (int i = 0; i < rozmiar; i++) {
        for (int j = 0; j < rozmiar; j++) {
            tabela[i][j] = rand() % 10;
        }
    }

    int suma = 0;
    for (int i = 0; i < rozmiar; i++) {
        for (int j = 0; j < rozmiar; j++) {
            std::cout << tabela[i][j] << " ";
        }

        std::cout << std::endl;
    }

    return 0;
}
