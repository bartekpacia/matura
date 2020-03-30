
/**
 * Użytkownik podaje 10 liczb całkowitych, które są elementami tablicy;
 * Program liczy ich sumę i średnią arytmetyczną.
 */

#include <iostream>

int main() {
    int rozmiar = 10;
    int liczby[rozmiar];

    for (int i = 0; i < rozmiar; i++) {
        std::cout << "Podaj liczbę: ";
        std::cin >> liczby[i];
    }

    int suma = 0;
    for (int i = 0; i < rozmiar; i++) {
        suma += liczby[i];
    }
    s std::cout << "Suma: " << suma << std::endl;

    float srednia = (float)suma / rozmiar;
    std::cout << "Średnia: " << srednia << std::endl;

    return 0;
}
