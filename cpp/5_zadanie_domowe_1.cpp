/**
 * Napisz program, który po wczytaniu dwóch liczb całkowitych w i k,
 * oznaczających liczbę wierszy i kolumn, gdzie są wstawione gwiazdki, obliczy
 * bok największego kwadratu, który można zbudować z tych gwiazdek. Program
 * powinien również wypisać liczbę niewykorzystanych gwiazdek (nie będą
 * potrzebne do wypełnienia kwadratu).
 */

#include <math.h>
#include <iostream>
#include <string>

int main() {
    int wiersze, kolumny = 0;
    std::cout << "Podaj liczbę wierszy: ";
    std::cin >> wiersze;
    std::cout << "Podaj liczbę kolumn: ";
    std::cin >> kolumny;

    if (!(wiersze > 0 && kolumny > 0)) {
        std::cout << "Podane niewłaściwe dane" << std::endl;
        getchar();
        return 0;
    }

    int gwiazdki = wiersze * kolumny;
    int bkwadrat = floor(sqrt(gwiazdki));
    int reszta = gwiazdki - (bkwadrat * bkwadrat);

    std::cout << "Bok najwiekszego kwadratu do zbudowania z tych gwiazdek to "
              << bkwadrat << std::endl;
    std::cout << "Reszta po zbudowaniu kwadratu to " << reszta << std::endl;

    getchar();
    return 0;
}