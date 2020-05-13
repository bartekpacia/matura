#include <iostream>

using namespace std;

// element stosu
struct ElementStosu {
    int dana;
    ElementStosu* nastepny;
};

// czy stos jest pusty
bool czyPusty(ElementStosu* S) { return !S; }

// przeczytaj element ze szczytu stosu
ElementStosu* gora(ElementStosu* S) { return S; }

// dodaj element na szczyt stosu, wartość elementu czyli dana, jest parametrem
// funkcji
void dodaj(int wartosc, ElementStosu** S) {
    ElementStosu* elem = new ElementStosu;

    elem->dana = wartosc;  // tutaj wpisujemy wartość do danej; wartość to
                           // parametr funkcji

    elem->nastepny = *S;

    *S = elem;
}

// pobierz element ze szczytu stosu
void pobierz(ElementStosu** S) {
    if (*S) {
        ElementStosu* elem = *S;

        *S = (*S)->nastepny;

        delete elem;
    }
}

int main() {
    // szczyt stosu; na poczatku stos jest pusty
    ElementStosu* stos = NULL;

    int i;

    // dodajemy 10 elementów całkowitych na stos (liczby od 1 do 10)

    for (i = 1; i <= 10; i++) {
        dodaj(i, &stos);
    }

    // czytamy i wyświetlamy elementy ze szczytu stosu i usuwamy je ze stosu
    while (!czyPusty(stos)) {
        cout << gora(stos)->dana << endl;
        pobierz(&stos);
    }

    return 0;
}