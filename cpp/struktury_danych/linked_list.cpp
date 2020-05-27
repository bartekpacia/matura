#include <iostream>

class ListElement {
   public:
    char value;
    ListElement* next;
    ListElement(char value, ListElement* next) : value(value), next(next) {}
};

// TODO: Finish impl
class Queue {
   private:
    ListElement* first;

   public:
    Queue() { first = NULL; };

    ~Queue();

    bool isEmpty() { return first == NULL; }

    char peek() { return first->value; };

    char insert(int index){
        // ListElement* newElem = new ListElement(value, NULL);
        // last = newElem;
    };

    char remove();
};