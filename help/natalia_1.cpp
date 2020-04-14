// Zadanie 1/86

#include <iostream>

using namespace std;

int szlaczek(char znak, int liczba_znakow) {
    for (int i = 0; i < liczba_znakow; i++) {
        cout << znak;
    }

    cout << endl;
    return znak;
}

int main() {
    char zn;
    int d;
    cout << "Podaj znak: ";
    cin >> zn;
    cout << "Podaj długosć: ";
    cin >> d;
    szlaczek(zn, d);
    return 0;
}