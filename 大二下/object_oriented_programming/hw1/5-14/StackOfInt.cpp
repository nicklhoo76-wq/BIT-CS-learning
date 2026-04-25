#include "StackOfInt.h"

struct StackOfInt::StackImp {
    std::vector<int> stack;
};

void StackOfInt::init() {
    s = new StackImp();
}

void StackOfInt::del() {
    delete s;
}

void StackOfInt::push(int val) {
    s->stack.push_back(val);
}

int StackOfInt::pop() {
    if (s->stack.empty) return -1;
    int val = s->stack.back();
    s->stack.pop_back();
    return val;
}

bool StackOfInt::empty() {
    return s->stack.empty();
}