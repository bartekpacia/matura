#include <iostream>

using namespace std;

class QueueElement {
   public:
    char value;
    QueueElement* prev;

    QueueElement(char value, QueueElement* prev) : value(value), prev(prev) {}
};

class Queue {
   private:
    QueueElement* front;
    QueueElement* back;

   public:
    Queue() {
        front = NULL;
        back = NULL;
    };

    ~Queue() {
        while (!isEmpty()) {
            dequeue();
        }
    };

    void enqueue(char value) {
        QueueElement* newElement = new QueueElement(value, NULL);

        if (isEmpty()) {
            front = newElement;
            back = newElement;
            back->prev = NULL;
        } else {
            back->prev = newElement;
            back = newElement;
            back->prev = NULL;
        }
    }

    char dequeue() {
        if (isEmpty()) {
            cout << "dequeue() failed - queue is empty" << endl;
            return NULL;
        }

        QueueElement* toBeDeleted = front;
        QueueElement toBeReturned = *front;

        front = front->prev;
        delete toBeDeleted;
        return toBeReturned.value;
    }

    bool isEmpty() { return front == NULL; }

    char peek() {
        if (isEmpty()) {
            cout << "peek() failed - queue is empty" << endl;
            return NULL;
        }

        return front->value;
    };
};

int main() {
    Queue* queue = new Queue;
    cout << "Created a queue at " << &queue << endl;

    int number_of_inputs;
    cout << "Enter the number of elements you want to enqueue ";
    cin >> number_of_inputs;

    // simple test to prove that this works
    queue->enqueue('D');
    queue->enqueue('U');
    queue->dequeue();
    queue->enqueue('P');
    queue->enqueue('A');

    cout << "- - - - - - - - - - - - - - - - " << endl;
    cout << "Displaying content of the queue: " << endl;

    while (!queue->isEmpty()) {
        cout << queue->dequeue() << endl;
    }

    return 0;
}
