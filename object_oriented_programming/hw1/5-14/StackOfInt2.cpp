#include "StackOfInt.h"

const int MAX_SIZE = 10;

struct StackOfInt::StackImp {
    int top;
    int stack[MAX_SIZE];
};

void StackOfInt::init() {
    s->top = -1;
}

void StackOfInt::del() {
    s->top = -1;
}

void StackOfInt::push(int val) {
    s->stack[++s->top];
}

int StackOfInt::pop() {
    if (s->stack.empty) return -1;
    int val = s->stack[s->top--];
    return val;
}

bool StackOfInt::empty() {
    return s->top == -1;
}