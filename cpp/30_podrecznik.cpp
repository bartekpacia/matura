/**
 * Napisz program, który wczyta liczbę n (1 <= n <= 9), wypełni tablicę n x n
 * wczytanymi z klawiatury liczbami, a następnie wypisze najczęściej występujący
 * element w tablicy. W przypadku, gdy kilka wartości występuje równie często,
 * należy wypisać element większy.
 */

#include <iostream>
#include <map>

int main() {
    int p{1}, k{10000}, rozmiar{0};

    std::cout << "Podaj rozmiar tablicy: ";
    std::cin >> rozmiar;

    int tab[rozmiar][rozmiar];  // deklaracja tablicy dwuwymiarowej (matrycy)

    srand(time(NULL));

    // Inicjalizacja – zapełnianie matrcycy losowymi liczbami
    for (int i{0}; i < rozmiar; i++) {
        for (int j{0}; j < rozmiar; j++) {
            tab[i][j] = rand() % (k - p + 1) + p;
        }
    }

    // Wyświetlanie matrycy
    for (int i{0}; i < rozmiar; i++) {
        for (int j{0}; j < rozmiar; j++) {
            std::cout << tab[i][j] << " ";
        }
        std::cout << std::endl;
    }

    // Tworzenie mapy [<liczba> -> <liczba jej wystąpień>] na podstawie matrycy
    std::map<int, int> wartosci;
    for (int i{0}; i < rozmiar; i++) {
        for (int j{0}; j < rozmiar; j++) {
            int obecny = tab[i][j];
            wartosci[obecny] += 1;
        }
    }

    // Znajdywanie <największej liczby wystąpień>
    int najczestsze_wystapienia{0};
    std::map<int, int>::iterator iterator;
    for (iterator = wartosci.begin(); iterator != wartosci.end(); iterator++) {
        int wystapienia = iterator->second;

        if (wystapienia > najczestsze_wystapienia) {
            najczestsze_wystapienia = wystapienia;
        }
    }

    // Znajdywanie liczb które wystąpiły <największa liczba wystąpień> razy
    std::map<int, int> najczestsze;  // najczęstsze (czyli są "ex aequo")
    for (iterator = wartosci.begin(); iterator != wartosci.end(); iterator++) {
        int liczba = iterator->first;
        int wystapienia = iterator->second;

        if (wystapienia == najczestsze_wystapienia) {
            najczestsze[liczba] = wystapienia;
        }
    }

    // The großes Finale – wyświetlanie mapy <najczestsze>
    for (iterator = najczestsze.begin(); iterator != najczestsze.end();
         iterator++) {
        int liczba = iterator->first;
        int wystapienia = iterator->second;

        std::cout << "Najczęściej wystąpiła liczba " << liczba << " ("
                  << wystapienia << ") razy" << std::endl;
    }

    return 0;
}