#include <iostream>

using namespace std;

class StackElement {
   public:
    char value;
    StackElement* next;

    StackElement(char value, StackElement* next) : value(value), next(next) {}
};

class Stack {
   private:
    StackElement* top;

   public:
    Stack() { top = NULL; }

    ~Stack() {
        while (!isEmpty()) {
            pop();
        }
    }

    void push(char value) {
        StackElement* newElement = new StackElement(value, top);

        top = newElement;
    }

    char pop() {
        if (isEmpty()) {
            cout << "pop() failed - stack is empty" << endl;
            return NULL;
        }

        StackElement* toBeDeleted = top;
        StackElement toBeReturned = *top;

        top = top->next;
        delete toBeDeleted;
        return toBeReturned.value;
    }

    bool isEmpty() { return top == NULL; }

    char peek() {
        if (isEmpty()) {
            cout << "peek() failed - stack is empty" << endl;
            return NULL;
        }

        return top->value;
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
        cout << stack->pop() << endl;
    }

    return 0;
}