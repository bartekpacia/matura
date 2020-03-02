#include <cstdlib>
#include <ctime>
#include <iostream>

int main() {
    int n = 5, m = 5;
    int p = 0, k = 2;
    int tab[n][m];

    srand(time(NULL));

    // Inicjalizacja
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            tab[i][j] = (rand() % (k - p + 1)) + p;
        }
    }

    // Liczenie sumy w wierszu
    for (int i = 0; i < n; i++) {
        int suma = 0;
        for (int j = 0; j < m; j++) {
            int obecny = tab[i][j];
            suma += obecny;
            std::cout << obecny << " ";
        }
        std::cout << "suma: " << suma << std::endl;
    }

    std::cout << "- - - - - - -  - - -" << std::endl;

    // Liczenie sumy w kolumnie
    for (int i = 0; i < n; i++) {
        int suma = 0;
        for (int j = 0; j < m; j++) {
            int obecny = tab[j][i];
            suma += obecny;
        }

        std::cout << "Suma w kolumie " << i << ": " << suma << std::endl;
    }

    // Sumowanie elementów z głównej przekątnej (lewa góra - prawy dół)
    // TYLKO W KWADRACIE (n == m)
    int suma_po_przekatnej_1 = 0;
    for (int i = 0; i < n; i++) {
        int obecny = tab[i][i];
        suma_po_przekatnej_1 += obecny;
    }

    int suma = 0;
    int max = INT_MIN;
    int min = INT_MAX;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            int obecny = tab[i][j];
            suma += obecny;

            if (obecny > max) {
                max = obecny;
            }

            if (obecny < min) {
                min = obecny;
            }
        }
    }

    std::cout << "- - - - - - - - - " << std::endl;
    std::cout << "Suma wszystkich: " << suma << std::endl;
    std::cout << "Największy element: " << max << std::endl;
    std::cout << "Najmniejszy element: " << min << std::endl;
    std::cout << "Suma elementów po przekątnej 1" << suma_po_przekatnej_1
              << std::endl;

    std::cout << "Suma elementów po przekątnej 2" << suma_po_przekatnej_2
              << std::endl;

    return 0;
}