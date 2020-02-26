
/**
 * Użytkownik podaje 10 liczb całkowitych, które są elementami tablicy;
 * Program ją wyświetla.
 */

#include <iostream>

int main() {
    int rozmiar = 10;
    int liczby[rozmiar];

    for (int i = 0; i < rozmiar; i++) {
        std::cout << "Podaj liczbę: ";
        std::cin >> liczby[i];
    }

    for (int i = 0; i < rozmiar; i++) {
        std::cout << "liczby[" << i << "] = " << liczby[i] << std::endl;
    }

    return 0;
}
