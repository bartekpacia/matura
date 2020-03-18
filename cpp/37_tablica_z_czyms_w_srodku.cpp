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
    int bok_duzego;
    int bok_malego = 4;
    cout << "Program zawsze dąży do tego, żeby marginesy wokół małego kwadratu "
            "były równe. Jeżeli nie będzie to możliwe, to zwiększy długość "
            "boków wewnętrzengo kwadratu."
         << endl;
    cout << "Podaj bok dużego kwadratu: ";
    cin >> bok_duzego;
    cout << "Podaj bok wewnętrzengo kwadratu: ";
    cin >> bok_malego;

    if (bok_duzego < 4) {
        cout << "Za małe n" << endl;
        return 1;
    }

    if (bok_duzego <= bok_malego + 1) {
        cout << "Bok małego jest za duży" << endl;
        return 1;
    }

    int tab[bok_duzego][bok_duzego];

    // Inicjalizacja (wypełnienie zerami)
    for (int i = 0; i < bok_duzego; i++) {
        for (int j = 0; j < bok_duzego; j++) {
            tab[i][j] = 1;
        }
    }

    int margin = (bok_duzego - bok_malego) / 2;

    for (int i = 0; i < bok_duzego; i++) {
        for (int j = 0; j < bok_duzego; j++) {
            if (i >= margin && i <= (bok_duzego - 1) - margin) {
                if (j >= margin && j <= (bok_duzego - 1) - margin) {
                    tab[i][j] = 0;
                }
            }
        }
    }

    // Wyświetlanie
    for (int i = 0; i < bok_duzego; i++) {
        for (int j = 0; j < bok_duzego; j++) {
            cout << tab[i][j];
        }
        cout << endl;
    }

    return 0;
}
