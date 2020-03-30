#include <iostream>

using namespace std;

int liczba_dni_do(int miesiac, int dzien);
int dni_w_miesiacu(int miesiac);

int main() {
    int miesiac, dzien;

    while (true) {
        cout << "Podaj miesiąc: ";
        cin >> miesiac;

        if (miesiac < 1 || miesiac > 12) {
            cout << "Niepoprawny numer miesiąca: " << miesiac << endl;
            continue;
        } else {
            cout << "Najwięcej dni w tym miesiącu to "
                 << dni_w_miesiacu(miesiac) << endl;
            break;
        }
    }

    while (true) {
        cout << "Podaj dzień: ";
        cin >> dzien;

        if (dzien < 1 || dzien > dni_w_miesiacu(miesiac)) {
            cout << "Niepoprawny dzień: " << dzien << endl;
            cout << "Najwiecej dni w tym miesiacu to "
                 << dni_w_miesiacu(miesiac) << endl;
            continue;
        } else {
            break;
        }
    }

    int dni_total = liczba_dni_do(miesiac, dzien);

    cout << "Od 1 stycznia (1, 1) do dnia (" << dzien << ") miesiąca ("
         << miesiac << ") upłynęło " << dni_total << " dni" << endl;

    return 0;
}

int liczba_dni_do(int miesiac, int dzien_miesiaca) {
    int dni = 0;

    dni += dzien_miesiaca;

    for (int i = 1; i < miesiac; i++) {
        dni += dni_w_miesiacu(i);
    }

    return dni - 1;
}

int dni_w_miesiacu(int miesiac) {
    int dni = 0;

    if (miesiac == 2) {
        dni = 28;
    } else if (miesiac <= 7) {
        if (miesiac % 2 == 0) {
            dni = 30;
        } else {
            dni = 31;
        }
    } else if (miesiac > 7) {
        if (miesiac % 2 == 0) {
            dni = 31;
        } else {
            dni = 30;
        }
    } else {
        cout << "Błąd w funkcji dni_w_miesiacu – żaden przypadek nie zadziałał"
             << endl;
        dni = 0;  // Niepoprawne dane, igornujemy
    }

    return dni;
}