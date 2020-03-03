/**
 * Zadanie 25
 * niedokończone bo okazało się że nie trzeba go robić
 */

#include <iostream>

int main() {
    int n = 2, m = 5;
    int p = 8, k = 9;
    int tab[n][m];

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            tab[i][j] = 0;
        }
    }

    for (int i = 0; i < m; i++) {
        int liczba_osob = 0;
        std::cout << "Podaj liczbę osób w dzień " << i << ": ";
        std::cin >> liczba_osob;

        tab[1][i] = liczba_osob;

        for (int j = 0; j < m; j++) {
            std::cout << tab[i][j] << std::endl;
        }
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            std::cout << tab[i][j] << " ";
        }
        std::cout << std::endl;
    }

    return 0;
}