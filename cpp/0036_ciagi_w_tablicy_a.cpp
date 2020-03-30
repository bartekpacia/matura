/* Zadanie 2 a)
Proszę napisać program, który wypełni liczbami całkowitymi tablicę
 n-elementową w następujący sposób:
1, 2, 3, 4, 5, 6, 7, 8, ..., n
*/

#include <iostream>

using namespace std;

int main() {
    int n;
    cout << "Podaj liczbę elemntów tablicy: ";
    cin >> n;

    if (n < 1) {
        cout << "Niewłaściwe dane" << endl;
        return 1;
    }

    int tabela[n];

    for (int i = 0; i < n; i++) {
        tabela[i] = i + 1;
    }

    for (int i = 0; i < n; i++) {
        cout << tabela[i] << " ";
    }
    cout << endl;

    return 0;
}
