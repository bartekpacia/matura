#include <cstdlib>
#include <ctime>
#include <iostream>
using namespace std;

int main() {
    int n;
    int g = 9;
    int d = 1;
    cout << "podaj rozmiar kwadratu ";
    cin >> n;
    int tablica[n][n];
    int przekatna[1][n];

    srand(time(NULL));

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            tablica[i][j] = rand() % (g - d + 1);
            cout << tablica[i][j] << " ";

            // i starczy
            // nie ma co robić za dużo w jednej pętli
        }
        cout << endl;
    }

    // Nowa pętla, tutaj przekleiłem twoją oryginalną logikę co wyciąłem z pętli
    // wyżej. Coś nie działa ale nie wiem co :[ 
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (i == j) {
                tablica[i][j] = przekatna[0][j];
            }
            if (i == n - j) {
                tablica[i][j] = przekatna[1][j];
            }
        }
    }

    cout << "- - - - - -" << endl;
    for (int i = 0; i < n; i++) {
        cout << przekatna[0][i] << " ";
    }

    cout << endl;
}