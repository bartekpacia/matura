#include <iostream>
#include <string>

int main() {
    int** pointer;
    int var1 = 10;
    int* var = &var1;
    pointer = &var;

    **pointer = 11;

    std::cout << "&pointer: " << &pointer << std::endl;
    std::cout << "pointer: " << pointer << std::endl;
    std::cout << "&var1: " << &var1 << std::endl;
    std::cout << "var1: " << var1 << std::endl;
    std::cout << "&var:" << &var << std::endl;
    std::cout << "var:" << var << std::endl;

    std::string bartek_pk{"debil"};
    std::string* pk = &bartek_pk;

    std::cout << "bartek pk to: " << *pk << std::endl;

    return 0;
}