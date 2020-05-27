#include <iostream>

using namespace std;
class QueueElement {
   public:
    char value;
    QueueElement* next;
    QueueElement(char value, QueueElement* next) : value(value), next(next) {}
};

// TODO: Finish impl
class Queue {
   private:
    QueueElement* front = NULL;
    QueueElement* back = NULL;

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
        back = newElement;

        if (isEmpty()) {
            front = newElement;
            back = newElement;
        } else {
            back->next = newElement;
            back = newElement;
        }
    }

    char dequeue() {
        if (isEmpty()) {
            cout << "dequeue() failed - queue is empty" << endl;
            return NULL;
        }

        QueueElement* toBeDeleted = front;
        QueueElement toBeReturned = *front;

        front = front->next;
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

    for (int i = 0; i < number_of_inputs; i++) {
        char input;
        cin >> input;
        queue->enqueue(input);
    }

    cout << "- - - - - - - - - - - - - - - - " << endl;
    cout << "Displaying content of the queue: " << endl;

    while (!queue->isEmpty()) {
        cout << queue->dequeue() << endl;
    }

    return 0;
}
