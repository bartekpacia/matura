#include <fstream>
#include <iostream>

int main() {
    std::ifstream file_input("liczby0044.txt");

    int smaller_than_1000 = 0;
    int last = -1;  // last smaller than 1000
    while (file_input) {
        int read_number;
        file_input >> read_number;

        if (read_number < 1000) {
            smaller_than_1000++;
            last = read_number;
        }
    }

    std::cout << "W pliku wejściowym jest " << smaller_than_1000
              << " liczb mniejszych od 1000" << std::endl;

    std::cout << "Ostatnia taka liczba to " << last << std::endl;
    return 0;
}
