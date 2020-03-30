/**
 * Napisz program, który narysuje trójkąt prostokątny z gwiazdek.
 */

#include <iostream>

int main() {
    int h = 0;

    std::cout << "Podaj max liczbę: ";
    std::cin >> h;

    for (int i = 1; i <= h; i++) {
        for (int j = 1; j <= i; j++) {
            std::cout << "*";
        }
        std::cout << std::endl;
    }

    return 0;
}
