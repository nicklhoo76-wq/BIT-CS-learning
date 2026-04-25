#include"Circle.h"

void Circle::getArea() {
	s = Pi * r * r;
}

void Circle::printArea() const {
	std::cout << "the area is " << s << std::endl;
}