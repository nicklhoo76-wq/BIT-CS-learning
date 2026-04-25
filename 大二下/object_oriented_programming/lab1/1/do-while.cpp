#include<iostream>

int main() {
	int i = 1, sum = 0;
	do {
		sum += i;
		i++;
	} while (i <= 10);
	std::cout << sum << std::endl;
}