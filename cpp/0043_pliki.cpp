#include <fstream>
#include <iostream>

using namespace std;

int main() {
    ofstream plik_wy("wyniki.txt");

    int zapisane = 0;

    if (plik_wy) {
        int liczba;
        do {
            cout << "Podaj liczbe: ";
            cin >> liczba;

            if (liczba % 2 == 0 && liczba != 0) {
                plik_wy << liczba << endl;
                zapisane++;
            }

        } while (liczba != 0);

        plik_wy.close();
        cout << "Zapisano " << zapisane << " liczb do pliku" << endl;
    } else {
        cout << "Wystąpił błąd podczas otwierania pliku!";
    }

    return 0;
}
