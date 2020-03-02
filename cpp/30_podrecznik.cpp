/**
 * Napisz program, który wczyta liczbę n (1 <= n <= 9), wypełni tablicę n x n
 * wczytanymi z klawiatury liczbami, a następnie wypisze najczęściej występujący
 * element w tablicy. W przypadku, gdy kilka wartości występuje równie często,
 * należy wypisać element większy.
 */

#include <iostream>
#include <map>

int main() {
    int p{1}, k{9}, rozmiar{0};

    std::cout << "Podaj rozmiar tablicy: ";
    std::cin >> rozmiar;

    int tab[rozmiar][rozmiar];

    srand(time(NULL));

    // Inicjalizacja
    for (int i{0}; i < rozmiar; i++) {
        for (int j{0}; j < rozmiar; j++) {
            tab[i][j] = rand() % (k - p + 1) + p;
        }
    }

    // Wyświetlanie
    for (int i{0}; i < rozmiar; i++) {
        for (int j{0}; j < rozmiar; j++) {
            std::cout << tab[i][j] << " ";
        }
        std::cout << std::endl;
    }

    // Logika
    std::map<int, int> wartosci;

    for (int i{0}; i < rozmiar; i++) {
        for (int j{0}; j < rozmiar; j++) {
            int obecny = tab[i][j];

            wartosci[obecny] += 1;
        }
    }

    int najczestsza_liczba{0};
    int najczestsze_wystapienia{0};

    std::map<int, int>::iterator iterator;
    for (iterator = wartosci.begin(); iterator != wartosci.end(); iterator++) {
        std::cout << "liczba: " << iterator->first << " razy "
                  << iterator->second << std::endl;

        int liczba = iterator->first;
        int wystapienia = iterator->second;

        if (wystapienia > najczestsze_wystapienia) {
            najczestsze_wystapienia = wystapienia;
            najczestsza_liczba = liczba;
        }
    }

    std::cout << "Najczęściej wystąpiła liczba " << najczestsza_liczba << " ("
              << najczestsze_wystapienia << ") razy" << std::endl;

    return 0;
}