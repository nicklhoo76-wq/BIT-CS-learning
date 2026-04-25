#include<iostream>
#include<vector>

class StackOfInt {
private:
	struct StackImp;
	StackImp *s;
public:
	void init();
	void del();
	void push(int);
	int pop();
	bool empty();
};