#include<iostream>
#include<numeric>
#include"fraction.h"
using namespace std;
Fraction Fraction::operator+(const Fraction& f) const {
	int n = numerator * f.denominator + denominator * f.numerator;
	int d = denominator * f.denominator;
	int gcd = std::gcd(abs(n), abs(d));
	return Fraction(n/gcd, d/gcd);
}
Fraction& Fraction::operator=(const Fraction& f){
	numerator = f.numerator;
	denominator = f.denominator;
	return *this;
}
Fraction::operator double() const {
	return static_cast<double>(numerator) / denominator;
}
ostream& operator<<(ostream& os, const Fraction& frac) {
	os << frac.numerator << "/" << frac.denominator;
	return os;
}