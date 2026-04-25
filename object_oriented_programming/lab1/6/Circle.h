#pragma once
#include<cmath>
#include<iostream>
class Circle {
	double r, s;
	const double Pi = 3.1415926;
public:
	Circle(double x):r(x), s(0){}
	void getArea();
	void printArea();
};