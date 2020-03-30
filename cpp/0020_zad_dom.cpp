/**
 * Wypełnić tablicę losowymi liczbami i obliczyć sumę liczb podzielnych przez 6
 * w tej tablicy.
 */

#include <cstdlib>
#include <ctime>
#include <iostream>

int main() {
    int rozmiar = 20;
    int liczby[rozmiar];

    srand(time(NULL));

    for (int i = 0; i < rozmiar; i++) {
        liczby[i] = rand() % 10;
    }

    int suma = 0;
    for (int i = 0; i < rozmiar; i++) {
        if (liczby[i] % 6 == 0) {
            suma += liczby[i];
        }
    }

    std::cout << "Suma liczb podzielnych przez 6: " << suma << std::endl;

    return 0;
}
