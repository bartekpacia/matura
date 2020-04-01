#include <math.h>

#include <iostream>

using namespace std;

float oblicz_pole_walca(int r, int h) {
    float pole_podstawy = 2 * M_PI * r * r;
    float pole_pow_bocznej = 2 * M_PI * r * h;

    float pole = pole_podstawy + pole_pow_bocznej;
    return pole;
}

float oblicz_objetosc_walca(int r, int h) {
    float objetosc = M_PI * r * r * h;
    return objetosc;
}

int main() {
    int r, h, dr;
    while (true) {
        cout << "Podaj promień walca: ";
        cin >> r;

        if (r <= 0) {
            cout << "Niepoprawna wartość promienia!" << endl;
            continue;
        } else {
            break;
        }
    }

    while (true) {
        cout << "Podaj wysokość walca: ";
        cin >> h;

        if (h <= 0) {
            cout << "Niepoprawna wartosc wysokosci!" << endl;
            continue;
        } else {
            break;
        }
    }
    while (true) {
        cout << "Podaj wielkość o ktorą chcesz zwiększyć promień walca: ";
        cin >> dr;

        if (dr <= 0) {
            cout << "Nie można powiększyć promienia o liczbe ujemną!" << endl;
            continue;
        } else {
            break;
        }
    }

    float pole = oblicz_pole_walca(r, h);
    float objetosc = oblicz_objetosc_walca(r, h);
    float pole_nowe = oblicz_pole_walca(r + dr, h);
    float objetosc_nowa = oblicz_objetosc_walca(r + dr, h);

    cout << "____________________________" << endl;
    cout << "Pole powierzchni walca o promieniu " << r << " i wysokosci " << h
         << " to " << pole << endl;
    cout << "Objetosc tego walca to " << objetosc << endl;
    cout << "Zwiększyłeś promień walca o " << dr << endl;
    cout << "Nowe pole powierzchni tego walca to " << pole_nowe << endl;
    cout << "Nowa objetosc tego walca to " << objetosc_nowa << endl;

    return 0;
}