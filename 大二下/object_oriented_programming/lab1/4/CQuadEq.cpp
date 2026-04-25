#include"CQuadEq.h"

void CQuadEq::FindRoot() {
	double re, im;
	if (a == 0) x1 = x2 = std::to_string(-c / b);
	else if (d == 0) x1 = x2 = std::to_string(-b / (2 * a));
	else if (d > 0) {
		x1 = std::to_string((b + sqrt(d)) / (-2 * a));
		x2 = std::to_string((b - sqrt(d)) / (-2 * a));
	}
	else {
		d = -d;
		re = b / (-2 * a);
		im = sqrt(d) / (-2 * a);
		im = (im > 0) ? im : -im;
		x1 = std::to_string(re) + "+" + std::to_string(im) + "i";
		x2 = std::to_string(re) + "-" + std::to_string(im) + "i";
	}
}
void CQuadEq::Show() {
	std::cout << "the roots are:\n x1 = " << x1 << "\n x2 = " << x2 << std::endl;
}