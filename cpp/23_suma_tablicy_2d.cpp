/**
 * Zadanie od pani, a właściwie kompilacja paru zadań. Doklejane w miarę jak
 * zadawała, dlatego ten plik jest taki wielki,
 * "Zawiera w sobie" zadanie 24 z podręcznika ()
 */

#include <cstdlib>
#include <ctime>
#include <iostream>

int main() {
    int n, m;

    std::cout << "Podaj rozmiar tablicy: ";
    std::cin >> n;

    m = n;
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
    // DZIAŁA POPRAWNIE TYLKO W KWADRACIE (czyli n == m)
    int suma_po_przekatnej_1 = 0;
    for (int i = 0; i < n; i++) {
        int obecny = tab[i][i];
        suma_po_przekatnej_1 += obecny;
    }

    // Sumowanie elementów z głównej przekątnej (prawa góra - lewy dół)
    // DZIAŁA POPRAWNIE TYLKO W KWADRACIE (czyli n == m)
    int suma_po_przekatnej_2 = 0;
    for (int i = 0; i < n; i++) {
        int obecny = tab[i][m - 1 - i];
        suma_po_przekatnej_2 += obecny;
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
    std::cout << "Suma elementów po przekątnej 1: " << suma_po_przekatnej_1
              << std::endl;

    std::cout << "Suma elementów po przekątnej 2: " << suma_po_przekatnej_2
              << std::endl;

    return 0;
}