/* Zadanie 2
Proszę napisać program, który wypełni liczbami całkowitymi tablicę
jednowymiarową n-elementową w następujący sposób: a) 1,2,3,4,5,6,... b)
1,2,4,7,11,16,22,29,37,... c) 0,1,2,3,0,1,2,3,0,1,2,3,0,1,2,3,... */

#include <iostream>

using namespace std;

int main() {
    int n = -1;
    cout << "Podaj liczbę elemntów tablicy" << endl;
    cin >> n;

    int tab1[n];
    int tab2[n];
    int tab3[n];

    for (int i = 0; i < n; i++) {
        tab1[i] = i;
    }

    cout << endl;

    int r0 = 1;
    int r1 = 1;
    for (int i = 0; i < n; i++) {
        if (i == 0) {
            tab2[0] = 1;
        } else {
            tab2[i] = i + tab2[i - 1];
        }
    }

    cout << endl;

    int diff = 0;
    for (int i = 0; i < n; i++) {
        if (diff == 4) {
            diff = 0;
        }

        tab3[i] = diff;
        diff++;
    }

    cout << endl;

    // Wyświetlanie danych
    for (int i = 0; i < n; i++) {
        cout << tab1[i] << " ";
    }
    cout << endl;

    for (int i = 0; i < n; i++) {
        cout << tab2[i] << " ";
    }
    cout << endl;

    for (int i = 0; i < n; i++) {
        cout << tab3[i] << " ";
    }
    cout << endl;

    return 0;
}
