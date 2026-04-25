#include<iostream>
#include"stack.h"
using namespace std;

int main() {
    Stack<int> IntStack;
    IntStack.push(5);
    IntStack.push(10);
    int m, n, p;
    IntStack.pop(m);
    IntStack.pop(n);
    cout << m << "," << n << endl;
    IntStack.pop(p);

    Stack<string> StrStack;
    StrStack.push("abc");
    StrStack.push("def");
    string x, y, z;
    StrStack.pop(x);
    StrStack.pop(y);
    cout << x << "," << y << endl;
    StrStack.pop(z);
}