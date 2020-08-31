#include <iostream>

using namespace std;
int main() {
    char plec;

    cout << "wpisz d jesli to dziewczyna lub c jesli to chlopak" << endl;
    cin >> plec;

    if (plec == 'd') {
        int wiek;
        cout << "wpisz wiek dziecka" << endl;
        cin >> wiek;

        if (wiek >= 10 && wiek <= 12) {
            cout << "witamy w druzynie";
        } else {
            cout << "niestety, nie kwalfikujesz sie" << endl;
        }
    } else {
        cout << "niestety, nie kwalfikujesz sie" << endl;
    }

    return 0;
}
