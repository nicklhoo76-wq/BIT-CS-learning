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
	B(int ii):i(ii){
		std::cout << "constructor of B" << std::endl;
	}
	~B(){
		std::cout << "destructor of B" << std::endl;
	}
	void f() const {}
};

class C : public B {
	A a;
public:
	C(int ii):B(ii), a(ii){
		std::cout << "constructor of C" << std::endl;
	}
	~C(){
		std::cout << "destructor of C" << std::endl;
	}
	void f() const {
		a.f();
		B::f();
	}
};

class D : public B{
	C c;
public:
	D(int ii):c(ii), B(ii){
		std::cout << "constructor of D" << std::endl;
	}
	~D() {
		std::cout << "destructor of D" << std::endl;
	}
};

int main() {
	D d(5);
}