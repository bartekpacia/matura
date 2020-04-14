// Zadanie 3 / 88
#include <cmath>
#include <iostream>

using namespace std;

float pole_kuli(int r) {
    float pole = 4 * M_PI * r * r;
    return pole;
}

float objetosc_kuli(int r) {
    float objetosc = (4 * M_PI * r * r * r) / 3;
    return objetosc;
}

int main() {
    float r;
    cout << "Podaj promień kuli: ";
    cin >> r;

    float pole = pole_kuli(r);
    float objetosc = objetosc_kuli(r);

    cout << "____________________________" << endl;
    cout << "Pole powierzchni tej kuli to " << pole << endl;
    cout << "Objetosc tej kuli to " << objetosc << endl;
    return 0;
}