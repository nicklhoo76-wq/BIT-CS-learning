#include<iostream>

int func(int x) {
	if (x == 1) return 1;
	else return x * func(x - 1);
}

int main() {
	int n;
	std::cout << "n = ";
	std::cin >> n;
	std::cout << "function called by its name:" << func(n) << std::endl;
	int (*func_ptr)(int);
	func_ptr = func;
	std::cout << "function called by its pointer:" << (*func_ptr)(n) << std::endl;
}