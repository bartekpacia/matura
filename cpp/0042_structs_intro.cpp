#include <time.h>

#include <iostream>
#include <vector>

using namespace std;

vector<string> imiona = {"Antek", "Bartosz", "Bartłomiej", "Kuba",   "Michał",
                         "Piotr", "Wojtek",  "Patryk",     "Roland", "Paweł"};

vector<string> nazwiska = {"Sobaszek", "Przybylak", "Tramś",     "Pacia",
                           "Matula",   "Wilk",      "Mieszczak", "Maciejończyk",
                           "Kamiński", "Przybyła"};

string generuj(vector<string> &wektor) {
    return wektor[rand() % wektor.size()];
}

struct Oceny {
    float matematyka;
    float fizyka;
    float informatyka;
    float angielski;
    float polski;
};

struct Uczen {
    string imie;
    string nazwisko;
};

int main() {
    srand(time(NULL));
    int liczba_uczniow = 10;
    Uczen uczniowie[liczba_uczniow];

    for (int i = 0; i < liczba_uczniow; i++) {
        Uczen uczen = {generuj(imiona), generuj(nazwiska)};

        uczniowie[i] = uczen;
    }

    for (int i = 0; i < liczba_uczniow; i++) {
        Uczen u = uczniowie[i];
        cout << "Imię: " << u.imie << ", nazwisko: " << u.nazwisko << endl;
    }

    return 0;
}
