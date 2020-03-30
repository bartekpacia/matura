
/**
 * Napisz program, który narysuje trójkąt równoramienny z gwiazdek.
 */

#include <iostream>

int main() {
    int h = 0;

    std::cout << "Podaj max liczbę: ";
    std::cin >> h;

    for (int i = 1; i <= h; i++) {
        int spacje = (h - i) * 2;

        for (int k = 0; k <= spacje / 2; k++) {
            std::cout << " ";
        }

        for (int j = 1; j <= (i * 2) - 1; j++) {
            std::cout << "*";
        }

        for (int k = 0; k <= spacje / 2; k++) {
            std::cout << " ";
        }

        std::cout << std::endl;
    }

    return 0;
}
