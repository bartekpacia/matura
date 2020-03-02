#include <cstdlib>
#include <ctime>
#include <iostream>

int main() {
    int n = 5, m = 5;
    int p = 2, k = 9;
    int tab[n][m];

    srand(time(NULL));

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            tab[i][j] = (rand() % (k - p + 1)) + p;
        }
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            std::cout << tab[i][j] << " ";
        }
        std::cout << std::endl;
    }

    int suma = 0;
    int najwieksza = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            suma += tab[i][j];

            if (tab[i][j] > najwieksza) {
                najwieksza = tab[i][j];
            }
        }

        std::cout << suma;
    }

    std::cout << "Suma: " << suma << std::endl;
    std::cout << "Największy element: " << najwieksza << std::endl;

    return 0;
}