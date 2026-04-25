#pragma once
#include<iostream>
class Fraction {
	int numerator;
	int denominator;
public:
	Fraction(int n = 1, int d = 1):numerator(n),denominator(d){}
	Fraction operator+(const Fraction& f) const;
	Fraction& operator=(const Fraction& f);
	operator double() const;
	friend std::ostream& operator<<(std::ostream& os, const Fraction& f);
};