#include"Triangle.h"
double Triangle::Area() const {
	double p = (x + y + z) / 2;
	return sqrt(p * (p - x) * (p - y) * (p - z));
}

int Triangle::IsTrig() const {
	if (x + y > z && x + z > y && y + z > x) return 1;
	else return 0;
}

void SumArea(Triangle t1, Triangle t2) {
	if (t1.IsTrig() && t2.IsTrig())
		std::cout << "\nthe sum of the triangles' area is:" << t1.Area() + t2.Area() << std::endl;
	else
		std::cout << "\nerror" << std::endl;
}