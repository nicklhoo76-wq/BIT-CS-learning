#include "CQuadEq.h"

int main() {
	int a, b, c;
	std::cout << "a = "; std::cin >> a;
	std::cout << "b = "; std::cin >> b;
	std::cout << "c = "; std::cin >> c;
	CQuadEq x(a, b, c);
	x.FindRoot();
	x.Show();
}