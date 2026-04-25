#pragma once
#include<iostream>
class Number {
	double n;
public:
	Number(double x):n(x){}
	const Number& operator+(const Number&);
	const Number& operator-(const Number&);
	const Number& operator*(const Number&);
	const Number& operator/(const Number&);
	Number& operator=(const Number&);
	operator int();
};