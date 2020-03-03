/**
 * Napisz program, który wczyta liczbę n, wypełni tablicę n x n wczytanymi z
 * klawiatury liczbami, a następnie policzy sumę cyfr wszystkich liczb
 * występujących w tablicy.
 */

// zrobione w pliku 23

#include <cstdlib>
#include <ctime>
#include <iostream>
#include <string>

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

    // Wyświetlenie
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            std::cout << tab[i][j] << " ";
        }

        std::cout << std::endl;
    }

    // Liczenie sumy w wierszu
    int suma_cyfr = 0;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            int obecny = tab[i][j];

            // Konwersja do stringa żeby łatwiej dostać się do poszczególnych
            // cyfr
            std::string s = std::to_string(obecny);
            for (int k = 0; k < s.length(); k++) {
                char znak_liczby = s[k];
                int cyfra = znak_liczby - '0';
                suma_cyfr += cyfra;
            }
        }
    }

    std::cout << "Suma cyfr wszystkich elementów tablicy: " << suma_cyfr
              << std::endl;

    return 0;
}