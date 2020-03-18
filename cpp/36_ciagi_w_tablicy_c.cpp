/* Zadanie 2
Proszę napisać program, który wypełni liczbami całkowitymi tablicę
jednowymiarową n-elementową w następujący sposób:
c) 0,1,2,3 0,1,2,3 0,1,2,3 0,1,2,3,... */

#include <iostream>

using namespace std;

int main() {
    int n;
    cout << "Podaj liczbę elemntów tablicy: ";
    cin >> n;

    int tabela[n];

    int zmienna = 0;
    for (int i = 0; i < n; i++) {
        if (zmienna > 3) {
            zmienna = 0;
        }

        tabela[i] = zmienna;
        zmienna++;
    }

    for (int i = 0; i < n; i++) {
        cout << tabela[i] << " ";
    }

    cout << endl;

    return 0;
}
