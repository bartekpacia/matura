#include <iostream>
#include <stack>

using namespace std;

// element stosu
struct StackElement {
    char value;
    StackElement* next;

    StackElement(char value, StackElement* next) : value(value), next(next) {}
};

bool isEmpty(StackElement* stackElement) { return stackElement == NULL; }

StackElement* top(StackElement* stackElement) { return stackElement; }

void push(char value, StackElement** stackElement) {
    StackElement* elem = new StackElement(value, *stackElement);

    *stackElement = elem;
}

void remove(StackElement** stackElement) {
    if (*stackElement) {
        StackElement* element = *stackElement;

        *stackElement = (*stackElement)->next;
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
        remove(&stack);
    }

    return 0;
}