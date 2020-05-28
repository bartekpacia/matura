#include <iostream>

using namespace std;

class Node {
   public:
    int data;

    Node(int data, Node* left, Node* right)
        : data(data), left(left), right(right) {}

    Node* left;
    Node* right;
};

// TODO: Finish impl
class Tree {
   public:
    Node* root;

    Tree() { root = NULL; }

    Node* insert(int data) {
        if (root = NULL) {
            root = new Node(data, NULL, NULL);
        } else {
            if (data < root->data) {
                root->left = insert(data /* WHERE? */);
            } else {
                root->right = insert(data /* WHERE? */);
            }
        }
    }
};

int main() { return 0; }
