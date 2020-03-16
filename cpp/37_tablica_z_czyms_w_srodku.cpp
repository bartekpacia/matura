/* Zadanie 3
Proszę napisać program, który wypełni tablicę dwuwymiarową kwadratową o
wymiarach n x n w podany niżej sposób. Bardziej ogólne zdanie: szerokość ramki k
podaje użytkownik. Wtedy należy zadbać o sprawdzenie poprawności k.

11111111
11111111
11000011
11000011
11000011
11000011
11111111
11111111 */

#include <iostream>

using namespace std;

int main() {
    int bok = -1;
    cout << "Podaj n (bok kwadratu): ";
    cin >> bok;

    // Dla liczb nieparzystych są dziwne wyniki
    // Dla mniejszych od 4 są naprawdę dziwne wyniki i nie wiem jak to obsłużyć
    if (bok < 4) {
        cout << "Za małe n" << endl;
        return 1;
    }

    int tab[bok][bok];

    // Inicjalizacja (wypełnienie zerami)
    for (int i = 0; i < bok; i++) {
        for (int j = 0; j < bok; j++) {
            tab[i][j] = 0;
        }
    }

    for (int i = 0; i < bok; i++) {
        for (int j = 0; j < bok; j++) {
            if (i >= bok / 4 && i < bok / 4 + bok / 2) {
                if (j >= bok / 4 && j < bok / 4 + bok / 2) {
                    tab[i][j] = 1;
                }
            }
        }
    }

    // Wyświetlanie
    for (int i = 0; i < bok; i++) {
        for (int j = 0; j < bok; j++) {
            cout << tab[i][j];
        }
        cout << endl;
    }

    return 0;
}
