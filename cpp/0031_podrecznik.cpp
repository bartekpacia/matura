/**
 * Zadanie 24
 *
 */

#include <cstdlib>
#include <ctime>
#include <iostream>

int main() {
    int n;

    std::cout << "Podaj rozmiar tablicy: ";
    std::cin >> n;

    int p = 0, k = 9;
    int tab[n][n];

    srand(time(NULL));

    // Inicjalizacja
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            tab[i][j] = (rand() % (k - p + 1)) + p;
        }
    }

    // Liczenie sumy w wierszu
    for (int i = 0; i < n; i++) {
        int suma = 0;
        for (int j = 0; j < n; j++) {
            int obecny = tab[i][j];
            suma += obecny;
            std::cout << obecny << " ";
        }
        std::cout << "suma: " << suma << std::endl;
    }

    std::cout << std::endl;
    std::cout << std::endl;

    // Sumowanie elementów z głównej przekątnej (lewa góra - prawy dół)
    int przekatna1[n];
    for (int i = 0; i < n; i++) {
        int obecny = tab[i][i];
        przekatna1[i] = obecny;
    }

    // Sumowanie elementów z głównej przekątnej (prawa góra - lewy dół)
    int przekatna2[n];
    for (int i = 0; i < n; i++) {
        int obecny = tab[i][n - 1 - i];
        przekatna2[i] = obecny;
    }

    for (int i = 0; i < n; i++) {
        std::cout << przekatna1[i] << " ";
    }

    std::cout << std::endl;

    for (int i = 0; i < n; i++) {
        std::cout << przekatna2[i] << " ";
    }

    std::cout << std::endl;

    return 0;
}
