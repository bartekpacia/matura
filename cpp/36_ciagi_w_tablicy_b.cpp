/* Zadanie 2
Proszę napisać program, który wypełni liczbami całkowitymi tablicę
jednowymiarową n-elementową w następujący sposób:
b) 1,2,4,7,11,16,22,29,37,...
*/

#include <iostream>

using namespace std;

int main() {
    int n;
    cout << "Podaj liczbę elemntów tablicy: ";
    cin >> n;

    int tabela[n];

    for (int i = 0; i < n; i++) {
        if (i == 0) {
            tabela[0] = 1;
        } else {
            tabela[i] = i + tabela[i - 1];
        }
    }

    for (int i = 0; i < n; i++) {
        cout << tabela[i] << " ";
    }

    cout << endl;

    return 0;
}
