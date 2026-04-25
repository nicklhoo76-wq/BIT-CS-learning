#pragma once
#include<cmath>
#include<iostream>
#include<string>
class CQuadEq {
	double a, b, c;
	double d = b * b - 4 * a * c;
	std::string x1, x2;
public:
	CQuadEq():a(1), b(2), c(1){}
	CQuadEq(double x, double y, double z):a(x), b(y), c(z){}
	void FindRoot();
	void Show();
};