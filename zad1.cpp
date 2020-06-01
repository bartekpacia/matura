#include <iostream>

using namespace std;

int main() {
    int a;
    int b;
    int c;

    cout << "Podaj pierwszą liczbę: ";
    cin >> a;

    cout << "Podaj drugą liczbę: ";
    cin >> b;

    cout << "Podaj trzecią liczbę: ";
    cin >> c;

    int najwieksza;
    if (a > b && a > c) {
        najwieksza = a;
    } else if (b > a && b > c) {
        najwieksza = b;
    } else if (c > a && c > b) {
        najwieksza = c;
    } else {
        cout << "Nie znaleziono największej" << endl;
        return 0;
    }

    float srednia = (a + b + c) / 3.0;

    cout << "Największa liczba: " << najwieksza << endl;
    cout << "Średnia: " << srednia << endl;

    return 0;
}
