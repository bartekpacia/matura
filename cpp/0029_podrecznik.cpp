/**
 * Zadanie 29
 * Napisz program, który wczyta liczbę n, wypełni tablicę n x n wczytanymi z
 * klawiatury liczbami, a następnie policzy i wypisze najmniejsze wartości z
 * każdego wiersza.
 */

#include <cstdlib>
#include <ctime>
#include <iostream>

int main() {
    int n, m;

    std::cout << "Podaj rozmiar tablicy: ";
    std::cin >> n;

    m = n;
    int p = 0, k = 9;
    int tab[n][m];

    srand(time(NULL));

    // Inicjalizacja
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            tab[i][j] = (rand() % (k - p + 1)) + p;
        }
    }

    // Wyświetlenie
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            std::cout << tab[i][j] << " ";
        }

        std::cout << std::endl;
    }

    std::cout << "- - - - - - - - - " << std::endl;

    // Logika
    for (int i = 0; i < n; i++) {
        int najmniejsza = INT_MAX;
        for (int j = 0; j < m; j++) {
            int obecny = tab[i][j];

            if (obecny < najmniejsza) {
                najmniejsza = obecny;
            }
        }

        std::cout << najmniejsza << std::endl;
    }

    return 0;
}