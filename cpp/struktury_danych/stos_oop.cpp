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

    StackElement pop() {
        StackElement* toBeDeleted = top;
        StackElement toBeReturned = *top;

        top = top->next;
        delete toBeDeleted;
        return toBeReturned;
    }
};

int main() {
    Stack* stack = new Stack();
    cout << "Created a stack at " << &stack << endl;

    int number_of_inputs;
    cout << "Enter the number of elements you want to push at the stack: ";
    cin >> number_of_inputs;

    for (int i = 0; i < number_of_inputs; i++) {
        char input;
        cin >> input;
        stack->push(input);
    }

    cout << "- - - - - - - - - - - - - - - - " << endl;
    cout << "Displaying content of the stack: " << endl;

    while (!stack->isEmpty()) {
        cout << stack->pop().value << endl;
    }

    return 0;
}