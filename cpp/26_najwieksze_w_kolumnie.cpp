/**
 * Zadanie 26
 * Napisz program, który wczyta liczbę n, wypełni tablicę n x n wylosowanymi
 * liczbami dwucyfrowymi, a następnie wypisze największe liczby z kolejnych
 * kolumn tablicy.
 */

#include <iostream>

int main() {
    int p = 10;
    int k = 99;
    int rozmiar = 0;

    std::cout << "Podaj rozmiar tablicy: ";
    std::cin >> rozmiar;

    int tab[rozmiar][rozmiar];

    srand(time(NULL));

    // Inicjalizacja
    for (int i = 0; i < rozmiar; i++) {
        for (int j = 0; j < rozmiar; j++) {
            tab[i][j] = rand() % (k - p + 1) + p;
        }
    }

    // Wyświetlenie
    for (int i = 0; i < rozmiar; i++) {
        for (int j = 0; j < rozmiar; j++) {
            std::cout << tab[i][j] << " ";
        }
        std::cout << std::endl;
    }

    // Logika
    for (int i = 0; i < rozmiar; i++) {
        int max = INT_MIN;

        for (int j = 0; j < rozmiar; j++) {
            int obecny = tab[j][i];

            if (obecny > max) {
                max = obecny;
            }
        }

        std::cout << "najwiekszy w kolumnie " << i << ": " << max << std::endl;
    }

    return 0;
}