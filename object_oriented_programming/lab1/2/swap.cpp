#include<iostream>

void swap_by_pointer(int *x, int *y) {
	int temp;
	temp = *x;
	*x = *y;
	*y = temp;
}
void swap_by_reference(int& x, int& y) {
	int temp;
	temp = x;
	x = y;
	y = temp;
}

int main() {
	int a = 1, b = 2, c =  3, d = 4;
	std::cout << "swap by pointer:\nbefore: a = " << a << " b = " << b << std::endl;
	swap_by_pointer(&a, &b);
	std::cout << "after: a = " << a << " b = " << b << std::endl;
	std::cout << "\nswap by reference:\nbefore: c = " << c << " d = " << d << std::endl;
	swap_by_reference(c, d);
	std::cout << "after: c = " << c << " d = " << d << std::endl;
}