#include <fstream>
#include <iostream>

int main() {
    std::ifstream file_input("trojki0045.txt");

    while (file_input) {
        int a, b, c;
        file_input >> a >> b >> c;

        if (a * b == c) {
            std::cout << a << " " << b << " " << c << std::endl;
        }
    }

    return 0;
}
