#include<iostream>
using namespace std;

class A;
class B {
public:
	void func(A);
};
class C {
public:
	void func(A);
};
class A {
private:
	int x;
	friend class B;
	friend void C::func(A);
public:
	void init(int n) {
		x = n;
	}
};
void B::func(A a) {
	cout << a.x << endl;
}
void C::func(A a) {
	cout << a.x << endl;
}

int main() {
	A a;
	a.init(1);
	B b;
	b.func(a);
	C c;
	c.func(a);
}