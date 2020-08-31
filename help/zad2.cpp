#include <iostream>

using namespace std;

int main() {
    int x;
    int y;

    cout << "Podaj wspolrzedna x: ";
    cin >> x;

    cout << "Podaj wspolrzedna y: ";
    cin >> y;

    int najwieksza;
    if (x == 0) {
        cout << "OY" << endl;
    }

    if (y == 0) {
        cout << "OX" << endl;
    }

    if (x != 0 && y != 0) {
        cout << "punkt nie lezy na osi" << endl;
    }

    return 0;
}
