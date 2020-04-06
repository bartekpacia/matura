#include <math.h>

#include <iostream>

using namespace std;

float oblicz_pole_kuli(int r) {
    float pole = 4 * M_PI * r * r;
    return pole;
}

float oblicz_objetosc_kuli(int r) {
    float objetosc = (4 * M_PI * r * r * r) / 3;
    return objetosc;
}

int main() {
    float r;
    while (true) {
        cout << "Podaj promień kuli: ";
        cin >> r;

        if (r <= 0) {
            cout << "Niepoprawna wartość promienia!" << endl;
            continue;
        } else {
            break;
        }
    }

    float pole = oblicz_pole_kuli(r);
    float objetosc = oblicz_objetosc_kuli(r);

    cout << "____________________________" << endl;
    cout << "Pole powierzchni tej kuli to " << pole << endl;
    cout << "Objetosc tej kuli to " << objetosc << endl;

    return 0;
}
