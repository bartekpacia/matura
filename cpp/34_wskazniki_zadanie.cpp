#include <iostream>
#include <string>

int main() {
    std::string tekst;

    std::cout << "Podaj tekst: ";
    std::cin >> tekst;

    // std::string::iterator iterator;
    // for (iterator = tekst.end(); iterator != tekst.begin(); iterator--) {
    //     std::cout << *iterator << std::endl;
    // }

    std::reverse(tekst.begin(), tekst.end());

    std::cout << tekst << std::endl;

    return 0;
}