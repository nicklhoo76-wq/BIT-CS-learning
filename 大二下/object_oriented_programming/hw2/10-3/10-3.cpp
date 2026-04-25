#include<iostream>

class A {
	static const int size = 5;
	int array[size];
	const int x;
	static int y;
public:
	inline A(int n): x(n){
		for (int i = 0; i < size; i++)
			array[i] = i + 1;
	}
	static void get() {
		std::cout << y << std::endl;
	}
	inline void print() {
		for (int i = 0; i < size; i++)
			std::cout << array[i] << std::endl;
		get();
	}
};
int A::y = 0;

int main() {
	A a(0);
	a.print();
}