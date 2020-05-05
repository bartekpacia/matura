#include <iostream>
#include <vector>

using namespace std;

struct Person {
    string name;
    int age;
    float mass;
    float height;
};

// QUEUE: FIRST IN, FIRST OUT
// STOS: LAST IN, FIRST OUT

struct Alliance {
    string name;
    int power;
    vector<Person> members;

    Alliance(string n, int p, vector<Person> m) {
        name = n;
        power = p;
        members = m;
    }
};

int main() {
    Alliance bartek_alliance{"SOJUSZ BARTKOW", INT_MAX, {}};  // NA STOSIE

    cout << bartek_alliance.name << endl;
    cout << bartek_alliance.power << endl;

    return 0;
}
