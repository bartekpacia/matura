#include <iostream>

using namespace std;

/**
 * Napisać program wyświetlający na ekranie kolejne liczby całkowite z
 *przedziału od 0 do a, które są podzielne przez 3 lub przez 4.
 *
 **/

int main() {
    int liczbunia;
    cout << "Podaj liczbe: ";
    cin >> liczbunia;

    for (int iksik = 0; iksik <= liczbunia; iksik++) {
        bool git = false;
        if (iksik % 4 == 0) {
            git = true;
        }
        if (iksik % 3 == 0) {
            git = true;
        }
        if (git) {
            cout << "git, iksik = " << iksik << endl;
        }
    }

    return 0;
}
