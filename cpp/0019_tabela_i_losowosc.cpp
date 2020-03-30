
/**
 * Program losuje 10 liczb naturalnych od 0 do 9. Następnie je wyświetla.
 */

#include <cstdlib>
#include <ctime>
#include <iostream>

int main() {
    int rozmiar = 10;
    int liczby[rozmiar];

    srand(time(NULL));

    for (int i = 0; i < rozmiar; i++) {
        liczby[i] = rand() % 10;
    }

    for (int i = 0; i < rozmiar; i++) {
        std::cout << "liczby[" << i << "] = " << liczby[i] << std::endl;
    }

    return 0;
}
