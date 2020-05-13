#include <iostream>
#include <stack>

using namespace std;

// element stosu
struct StackElement {
    char value;
    StackElement* next;

    StackElement(char value, StackElement* next) : value(value), next(next) {}
};

bool isEmpty(StackElement* elementStosu) { return elementStosu == NULL; }

StackElement* top(StackElement* elementStosu) { return elementStosu; }

void push(char wartosc, StackElement** elementStosu) {
    StackElement* elem = new StackElement(wartosc, *elementStosu);

    *elementStosu = elem;
}

// pobierz element ze szczytu stosu
void pobierz(StackElement** elementStosu) {
    if (*elementStosu) {
        StackElement* element = *elementStosu;

        *elementStosu = (*elementStosu)->next;
        delete element;
    }
}

int main() {
    StackElement* stack = NULL;

    // for (int i = 1; i <= 5; i++) {
    //     char znak_od_uzytkownika;
    //     cin >> znak_od_uzytkownika;
    //     push(znak_od_uzytkownika, &stack);
    // }

    cout << &stack << endl;

    push('p', &stack);
    push('a', &stack);
    push('c', &stack);
    push('i', &stack);
    push('a', &stack);

    cout << "Displaying content of the stack: " << endl;

    while (!isEmpty(stack)) {
        cout << top(stack)->value << endl;
        pobierz(&stack);
    }

    return 0;
}