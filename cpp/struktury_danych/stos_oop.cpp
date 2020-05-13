#include <iostream>
#include <stack>

using namespace std;

struct StackElement {
    char value;
    StackElement* next;

    // StackElement(char value) : value(value) {}
    StackElement(char value, StackElement* next) : value(value), next(next) {}
};

struct Stack {
    StackElement* top = NULL;

    bool isEmpty() { return top == NULL; }

    void push(char value) {
        cout << "begin push()" << endl;
        StackElement* newElement = new StackElement(value, top);
        cout << "middle push()" << endl;

        // == if top points to something
        if (top) {
            cout << "top points to something." << endl;
        } else {
            cout << "top doens't point to anything!" << endl;
        }
        top = newElement;

        cout << "end push()" << endl;
    }

    void remove() {
        StackElement* toBeReturned = top;

        top = top->next;
        // FIXME: Memory leak
        // delete toBeReturned;
    }
};

int main() {
    Stack* stack = new Stack();

    // for (int i = 1; i <= 5; i++) {
    //     char znak_od_uzytkownika;
    //     cin >> znak_od_uzytkownika;
    //     push(znak_od_uzytkownika, &stack);
    // }

    cout << &stack << endl;

    stack->push('p');
    stack->push('a');
    stack->push('c');
    stack->push('i');
    stack->push('a');

    cout << "Displaying content of the stack: " << endl;

    while (!stack->isEmpty()) {
        cout << stack->top->value << endl;
        stack->remove();
    }

    return 0;
}