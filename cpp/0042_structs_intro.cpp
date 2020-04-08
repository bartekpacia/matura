#include <time.h>

#include <iostream>
#include <vector>

using namespace std;

vector<string> imiona = {"Antek", "Bartosz", "Bartłomiej", "Kuba",   "Michał",
                         "Piotr", "Wojtek",  "Patryk",     "Roland", "Paweł"};

vector<string> nazwiska = {"Sobaszek", "Przybylak", "Tramś",     "Pacia",
                           "Matula",   "Wilk",      "Mieszczak", "Maciejończyk",
                           "Kamiński", "Przybyła"};

string generuj(vector<string>& wektor) {
    return wektor[rand() % wektor.size()];
}

int generuj(int min, int max) { return rand() % (max - min + 1) + min; }

struct Oceny {
    int matematyka;
    int fizyka;
    int informatyka;
    int angielski;
    int polski;
};

struct Uczen {
    string imie;
    string nazwisko;
    Oceny* oceny;
};

int main() {
    srand(time(NULL));
    int liczba_uczniow = 10;
    Uczen uczniowie[liczba_uczniow];

    for (int i = 0; i < liczba_uczniow; i++) {
        Oceny oceny = {generuj(1, 6), generuj(1, 6), generuj(1, 6),
                       generuj(1, 6), generuj(1, 6)};

        Uczen uczen = {generuj(imiona), generuj(nazwiska), &oceny};

        uczniowie[i] = uczen;
    }

    for (int i = 0; i < liczba_uczniow; i++) {
        Uczen u = uczniowie[i];
        cout << u.imie << " " << u.nazwisko
             << ", matematyka: " << u.oceny->matematyka << endl;
    }

    return 0;
}
