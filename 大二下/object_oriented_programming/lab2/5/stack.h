#pragma once
#include<vector>
#include<string>
#include<iostream>

template <typename T>
class Stack {
    std::vector<T> stack;
    int top;
public:
    Stack() : top(0) {}
    void push(T element) {
        stack.push_back(element);
        top++;
    }
    void pop(T& element) {
        if (!empty()) {
            top--;
            element = stack[top];
        }
        else {
            std::cout << "error: no elements left.\n";
            element = T();
        }
    }
    bool empty() {
        return top <= 0;
    }
};