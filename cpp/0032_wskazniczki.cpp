#include <iostream>

int main() {
    int *pointer;
    *pointer = 2;

    std::cout << "pointer value: " << pointer << std::endl;
    std::cout << "pointer points to value :" << *pointer << std::endl;

    return 0;
}