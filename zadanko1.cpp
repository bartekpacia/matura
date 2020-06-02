#include <iostream>

using namespace std;

int main() {
    int max;
    cout << "wpisz max: ";
    cin >> max;

    for (int i = 0; i < max; i++) {
        bool wyswietlic = false;

        if (i % 3 == 0) {
            wyswietlic = true;
        }

        if (i % 4 == 0) {
            wyswietlic = true;
        }

        if (wyswietlic) {
            cout << i << endl;
        }
    }

    return 0;
}
