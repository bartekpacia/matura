#include <iostream>

int main() {
    int n = 10, m = 10;
    int tab[n][m];

    // uwaga kupa, może być 3x krótsze
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (i % 2 == 0) {
                if (j % 2 == 0) {
                    tab[i][j] = 0;
                } else {
                    tab[i][j] = 7;
                }
            } else {
                if (j % 2 == 0) {
                    tab[i][j] = 7;
                } else {
                    tab[i][j] = 0;
                }
            }
        }
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            std::cout << tab[i][j] << " ";
        }
        std::cout << std::endl;
    }

    return 0;
}