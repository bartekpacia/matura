#include <iostream>

using namespace std;

struct StackElement {
    char value;
    StackElement* next;

    StackElement(char value, StackElement* next) : value(value), next(next) {}
};

struct Stack {
    StackElement* top = NULL;

    bool isEmpty() { return top == NULL; }

    void push(char value) {
        StackElement* newElement = new StackElement(value, top);

        top = newElement;
    }

    void remove() {
        StackElement* toBeReturned = top;

        top = top->next;
        // FIXME: Memory leak???
        delete toBeReturned;
    }
};

int main() {
    Stack* stack = new Stack();
    cout << "Adres stosu: " << &stack << endl;

    for (int i = 1; i <= 5; i++) {
        char znak_od_uzytkownika;
        cin >> znak_od_uzytkownika;
        stack->push(znak_od_uzytkownika);
    }

    cout << "Displaying content of the stack: " << endl;

    while (!stack->isEmpty()) {
        cout << stack->top->value << endl;
        stack->remove();
    }

    return 0;
}