#include <iostream>

using namespace std;

unsigned long int silnia_rekurencyjnie(unsigned long int n) {
    if (n == 1 || n == 0) {
        return 1;
    } else {
        return n * silnia_rekurencyjnie(n - 1);
    }
}

int silnia_iteracyjnie(int n) {
    unsigned long int wynik = 1;

    for (unsigned int i = 1; i <= n; i++) {
        wynik = wynik * i;
    }

    return wynik;
}

int main() {
    int a;

    cout << "Podaj liczbę z której chcesz obliczyć silnię: ";
    cin >> a;

    cout << "Silnia  rekurencyjnie: " << silnia_rekurencyjnie(a) << endl;
    cout << "Silnia  iteracyjnie: " << silnia_iteracyjnie(a) << endl;

    return 0;
}
