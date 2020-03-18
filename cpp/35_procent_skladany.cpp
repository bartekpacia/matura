/* Zadanie 1
Klient wpłaca do banku pewną kwotę pieniędzy (v0). Ile bank wypłaci mu po n
latach, jeżeli odsetki są dopisywane co kwartał? Zakładamy, że w całym okresie
oszczędzania oprocentowanie jest stałe i wynosi r% w skali roku (procent
składany). Dane: v0, n, r - podaje użytkownik Program powinien również zadbać o
poprawność wprowadzanych danych.

Procent składany na wiki:
https://pl.wikipedia.org/wiki/Procent_sk%C5%82adany
*/

#include <math.h>
#include <iostream>

using namespace std;

int main() {
    int n;
    int m = 4;
    double v0;
    double r;
    cout << "Podaj kwotę wpłaconą do banku: ";
    cin >> v0;
    cout << "Podaj liczbę lat, na którą chcesz zdeponować kwotę: ";
    cin >> n;
    cout << "Podaj roczną stopę oprocentowania (np. 5% = 0.05) ";
    cin >> r;

    if (v0 <= 0) {
        cout << "Nie możesz wpłacić mnieeeej niż zeeeeeroooo." << endl;
        return 1;
    }

    if (n <= 0) {
        cout << "Za krótki okres zdeponowania" << endl;
        return 1;
    }

    if (r <= 0) {
        cout << "Za niska stopa oprocentowania" << endl;
        return 1;
    }

    double v = v0 * pow(1 + r / m, m * n);

    cout << "Kwota końcowa: " << v << endl;

    return 0;
}
