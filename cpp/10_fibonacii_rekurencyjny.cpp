/**
 * Napisz program, który oblicza ciąg Fibonacciego za pomocą rekurencji.
 */

#include <iostream>

int fibonacci(int input) {
    if (input == 0) {
        return 0;
    } else if (input == 1) {
        return 1;
    } else {
        return fibonacci(input - 1) + fibonacci(input - 2);
    }
}

int main() {
    int max = 0;

    std::cout << "Podaj max liczbę: ";
    std::cin >> max;

    int fib = fibonacci(max);

    std::cout << "liczba ciągu: " << max << " wartość: " << fib << std::endl;

    return 0;
}
