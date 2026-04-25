#include "Circle.h"
using namespace std;
int main() {
	double r1, r2;
	cout << "r1 = "; cin >> r1;
	cout << "r2 = "; cin >> r2;
	const Circle c1(r1);
	Circle c2(r2);
	//c1.getArea();
	//这一行出现报错。因为非常成员函数可能会修改成员变量，与相应对象是常量矛盾，
	//所以常对象无法调用非常成员函数。
	c1.printArea();
	c2.getArea();
	c2.printArea();
}