#include <iostream>

using namespace std;

int szlaczek(char znak, int liczba_znakow) {
    for (int i = 0; i < liczba_znakow; i++) {
        cout << znak;
    }

    cout << endl;
    return znak;  // zwracamy kod ASCII znaku (występuje rzutowanie char -> int)
}

int main(int argc, char const *argv[]) {
    int dlugosc;
    char znaczek;
    cout << "Podaj znaczek: ";
    cin >> znaczek;

    cout << "Podaj długość szlaczka: ";
    cin >> dlugosc;

    int kod_znaku = szlaczek(znaczek, dlugosc);
    cout << "Kod znaku w szlaczku: " << kod_znaku << endl;

    return 0;
}
