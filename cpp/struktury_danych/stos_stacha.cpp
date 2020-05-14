#include <iostream>

using namespace std;

struct stackElem

{
    stackElem* nxt;

    int dana;
};

bool isEmpty(stackElem* S)

{
    return !S;
}

stackElem* top(stackElem* S)

{
    return S;
}

void add(int value, stackElem** S)

{
    stackElem* elem = new stackElem;

    elem->dana = value;

    elem->nxt = *S;

    *S = elem;
}

void get(stackElem** S)

{
    if (*S)

    {
        stackElem* elem = *S;

        *S = (*S)->nxt;

        delete elem;
    }
}

int main()

{
    stackElem* S = NULL;

    int i;

    // fill the stack
    for (i = 1; i <= 10; i++)

    {
        add(i, &S);
    }

    while (!isEmpty(S))

    {
        cout << top(S)->dana << endl;

        get(&S);
    }

    return 0;
}