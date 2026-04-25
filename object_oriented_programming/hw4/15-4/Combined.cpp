#include<iostream>
class A {
	int i;
public:
	A(int ii):i(ii){}
	~A(){}
	void f() const {}
};

class B {
	int i;
public:
	B(int ii):i(ii){}
	~B(){}
	virtual void f() const {
		std::cout << "f() of B" << std::endl;
	}
};

class C : public B {
	A a;
public:
	C(int ii):B(ii), a(ii){}
	~C(){}
	void f() const {
		a.f();
		B::f();
		std::cout << "f() of C" << std::endl;
	}
};

int main() {
	C c(47);
	B& b = c;
	b.f();
}