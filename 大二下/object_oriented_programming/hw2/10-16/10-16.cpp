#include<iostream>
#include "second.h"

namespace Name = MyName;
void using_scope_res() {
	Name::func(1);
	Name::func3(2.0);
}
void without_scope_res() {
	using namespace Name;
	func2(2, 3);
	func4(4.0, 5.0);
}
namespace MyName {
	void func(int x) { std::cout << x << std::endl; }
	void func2(int x, int y) { std::cout << x + y << std::endl; }
	void func3(double x) { std::cout << x << std::endl; }
	void func4(double x, double y) { std::cout << x / y << std::endl; }
}
int main() {
	using_scope_res();
	without_scope_res();
}