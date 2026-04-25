#include<iostream>
using namespace std;

int func(double x) {
	return x + 1;
}

int main() {
	int (*fp)(double);
	fp = func;
	cout << (*fp)(1.0) << endl;
}