#include <iostream>

using namespace std;

int main() {
    int suma = 0;

    for (int i = 1; i <= 31; i = i + 3) {
        suma = suma + i;
    }

    cout << suma << endl;

    return 0;
}
