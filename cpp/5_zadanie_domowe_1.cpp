/**
 * Napisz program, który po wczytaniu dwóch liczb całkowitych w i k,
 * oznaczających liczbę wierszy i kolumn, gdzie są wstawione gwiazdki, obliczy
 * bok największego kwadratu, który można wypełnić tymi gwiazdkami. Program
 * powinien również wypisać liczbę niewykorzystanych gwiazdek (nie będą
 * potrzebne do wypełnienia kwadratu).
 */

#include <iostream>
#include <string>

int main() {
    int wiersze, kolumny = 0;
    std::cout << "Podaj liczbę wierszy: " << std::endl;
    std::cin >> wiersze;
    std::cout << "Podaj liczbę kolumn: " << std::endl;
    std::cin >> kolumny;

    if (!(wiersze > 0 && kolumny > 0)) {
        std::cout << "Podane niewłaściwe dane" << std::endl;
        getchar();
        return 0;
    }

    int najwiekszy_bok = 0;
    if (wiersze <= kolumny) {
        najwiekszy_bok = wiersze;
    } else {
        najwiekszy_bok = kolumny;
    }

    int gwiazdki = wiersze * kolumny;
    int gwiazdki_w_kwadracie = najwiekszy_bok * najwiekszy_bok;
    int niewykorzystane_gwiazdki = gwiazdki - gwiazdki_w_kwadracie;

    std::cout << "Bok największego kwadratu: " << najwiekszy_bok << std::endl;
    std::cout << "Liczba niewykorzystanych gwiazdek: "
              << niewykorzystane_gwiazdki << std::endl;

    getchar();
    return 0;
}