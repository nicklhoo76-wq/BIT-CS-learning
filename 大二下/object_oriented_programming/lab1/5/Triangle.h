#pragma once
#include<cmath>
#include<iostream>
class Triangle {
	double x, y, z;
	double Area();
public:
	Triangle(double a, double b, double c) :x(a), y(b), z(c) {}
	int IsTrig();
	friend void SumArea(Triangle t1, Triangle t2);
};