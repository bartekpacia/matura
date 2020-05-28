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

Node* insertToTree(Node* root, int data) {
    if (root == NULL) {
        root = new Node(data, NULL, NULL);
    } else {
        if (data < root->data) {
            root->left = insertToTree(root->left, data);
        } else {
            root->right = insertToTree(root->right, data);
        }
    }
    return root;
}

void printTree(Node* root, int level) {
    if (root == NULL) {
        cout << "Level " << level;
    }

    for (int i = 1; i <= level; i++) {
        cout << "     " << endl;
        cout << root->data << endl;
    }
    printTree(root->left, level + 1);
    printTree(root->right, level + 1);
}

// shit
Node* whenTwoChildren(Node* q, Node** p) {
    if (q->right != NULL) {
        q->right = whenTwoChildren(q->right, &*p);
    } else {
        (*p)->data = q->data;
        *p = q;
        q = q->left;
    }
    return q;
}

Node* removeFromTree(Node* root, int data, bool* exists) {
    *exists = false;
    Node* helper;
    if (root != NULL) {
        if (data < root->data) {
            root->left = removeFromTree(root->left, data, exists);
        } else if (data > root->data) {
            root->right = removeFromTree(root->right, data, exists);
        } else {
            helper = root;
            if (helper->right == NULL) {
                root = helper->left;
            } else if (helper->left == NULL) {
                root = helper->right;
            } else {
                helper->left = whenTwoChildren(helper->left, &helper);
            }
            delete helper;
            *exists = false;
        }
    }
    return root;
}

int main() {
    int number;
    Node* root;
    bool exists = false;

    cout << "Building a tree..." << endl;
    cout << "------------------" << endl;
    cout << "Enter an array of numbers ending with a \"0\"" << endl;
    cin >> number;

    if (number > 0) {
        root = NULL;
        while (number) {
            root = insertToTree(root, number);
            cin >> number;
        }
        cout << "------------------" << endl;
        cout << "That's how the tree looks like: " << endl;
        printTree(root, number);
        cout << "------------------" << endl;
    }
}