/**
 * Zadanie 27
 * Napisz program, który wczyta liczbę n, wypełni tablicę n x n wylosowanymi
 * liczbami dwucyfrowymi, a następnie wypisze liczby w formie szachownicy.
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

    // Wyświetlanie
    for (int i = 0; i < rozmiar; i++) {
        for (int j = 0; j < rozmiar; j++) {
            std::cout << tab[i][j] << " ";
        }
        std::cout << std::endl;
    }

    // Logika
    for (int i = 0; i < rozmiar; i++) {
        for (int j = 0; j < rozmiar; j++) {
            int obecny = tab[i][j];

            if ((i + j) % 2 == 1) {
                tab[i][j] = -1;
            }
        }
    }

    std::cout << "- - - - - - - -" << std::endl;

    // Wyświetlanie
    for (int i = 0; i < rozmiar; i++) {
        for (int j = 0; j < rozmiar; j++) {
            if (tab[i][j] == -1) {
                std::cout << " ";
            } else {
                std::cout << tab[i][j] << " ";
            }
        }
        std::cout << std::endl;
    }

    return 0;
}