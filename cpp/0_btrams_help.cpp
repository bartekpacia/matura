#include <cstdlib>
#include <ctime>
#include <iostream>
using namespace std;

int main() {
    int n;
    int tablica[n][n];
    int g = 100;
    int d = 0;
    int przekatna[1][n];
    cout << "podaj rozmiar kwadratu ";
    cin >> n;

    srand(time(NULL));

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            tablica[i][j] = rand() % (g - d + 1);
            cout << tablica[i][j] << " ";

            if (i == j) {
                tablica[i][j] = przekatna[0][j];
            }
            if (i == n - j) {
                tablica[i][j] = przekatna[1][j];
            }
        }
        cout << endl;
    }

    for (int i = 0; i < n; i++) {
        cout << przekatna[0][i] << " ";
    }
}