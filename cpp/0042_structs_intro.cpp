#include <time.h>

#include <iostream>
#include <vector>

using namespace std;

/*
 * Uwaga
 * Napisane na szybko, nieprzetestowane dokładnie.
 * Kompiluje się i działa, ale może zawierać błędy.
 */

vector<string> imiona = {"Antek", "Bartosz", "Bartłomiej", "Kuba",   "Michał",
                         "Piotr", "Wojtek",  "Patryk",     "Roland", "Paweł"};

vector<string> nazwiska = {"Sobaszek", "Przybylak", "Tramś",     "Pacia",
                           "Matula",   "Wilk",      "Mieszczak", "Maciejończyk",
                           "Kamiński", "Przybyła"};

string generuj(vector<string>& wektor) {
    return wektor[rand() % wektor.size()];
}

vector<int> generuj(int size, int min, int max) {
    vector<int> wynik;
    for (int i = 0; i < size; i++) {
        wynik.push_back(rand() % (max - min + 1) + min);
    }

    return wynik;
}

float licz_srednia(vector<int> oceny) {
    float srednia = 0;
    for (int i = 0; i < oceny.size(); i++) {
        srednia += oceny[i];
    }

    return srednia / oceny.size();
}

struct Oceny {
    vector<int> matematyka;
    vector<int> fizyka;
    vector<int> informatyka;
    vector<int> angielski;
    vector<int> polski;

    Oceny() {
        matematyka = generuj(12, 1, 6);
        fizyka = generuj(10, 1, 6);
        informatyka = generuj(7, 1, 6);
        angielski = generuj(13, 1, 6);
        polski = generuj(4, 1, 6);
    }

    float srednia_ze_wszystkich() {
        float matematyka_srednia = licz_srednia(matematyka);
        float fizyka_srednia = licz_srednia(fizyka);
        float informatyka_srednia = licz_srednia(informatyka);
        float angielski_srednia = licz_srednia(angielski);
        float polski_srednia = licz_srednia(polski);

        // Można zrobić to duzo lepiej ale nie chce mi sie
        return (matematyka_srednia + fizyka_srednia + informatyka_srednia +
                angielski_srednia + polski_srednia) /
               5;
    }
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
        Oceny* oceny = new Oceny();

        Uczen uczen = {generuj(imiona), generuj(nazwiska), oceny};

        uczniowie[i] = uczen;
    }

    for (int i = 0; i < liczba_uczniow; i++) {
        Uczen u = uczniowie[i];
        cout << u.imie << " " << u.nazwisko
             << ", średnia ze wszystkich przedmiotów: "
             << u.oceny->srednia_ze_wszystkich() << endl;
    }

    return 0;
}
