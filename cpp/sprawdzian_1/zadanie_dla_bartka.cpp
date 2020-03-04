#include <iostream>

int main() {
    int suma = 0;
    int ilosc_liczb = 0;
    int ilosc_ok_liczb = 0;  // ok = jednocyfrowa i parzysta
    int tab[5];

    int i = 0;
    while (suma < 20 && ilosc_liczb != 5) {
        int wczytana = 0;
        std::cin >> wczytana;
        std::cout << "wczytana: " << wczytana << std::endl;

        // Czy jest jednocyfrowa i parzysta (0 liczymy jako parzysta)
        if (wczytana >= -9 && wczytana <= 9 && wczytana % 2 == 0) {
            std::cout << "wczytana jest jednocyfrowa parzysta" << std::endl;

            suma += wczytana;
            tab[i] = wczytana;
            ilosc_ok_liczb++;
        }

        i++;
        ilosc_liczb++;
    }

    for (int j = 0; j < ilosc_ok_liczb; j++) {
        std::cout << "tab[" << j << "] = " << tab[j] << std::endl;
    }

    std::cout << "Zostało wczytane " << ilosc_liczb << " liczb" << std::endl;
    std::cout << "Zostało dodane " << ilosc_ok_liczb << " liczb" << std::endl;
    std::cout << "Suma jednocyfrowych i parzystych: " << suma << std::endl;

    getchar();
    return 0;
}