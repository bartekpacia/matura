#include <iostream>

class QueueElement {
   public:
    char value;
    QueueElement* next;
    QueueElement(char value, QueueElement* next) : value(value), next(next) {}
};

// TODO: Finish impl
class Queue {
   private:
    QueueElement* first;
    QueueElement* last;

   public:
    Queue() { first = last = NULL; };

    ~Queue();

    bool isEmpty() { return first == NULL; }

    char peek() { return first->value; };

    char add(char value) {
        QueueElement* newElem = new QueueElement(value, NULL);
        last = newElem;
    };

    char remove();
};