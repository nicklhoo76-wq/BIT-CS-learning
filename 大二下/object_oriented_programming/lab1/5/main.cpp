#include "Triangle.h"
using namespace std;
int main() {
	double x1, y1, z1;
	double x2, y2, z2;
	cout << "the first triangle's edges are:" << endl;
	cin >> x1 >> y1 >> z1;
	cout << "\nthe second triangle's edges are:" << endl;
	cin >> x2 >> y2 >> z2;
	Triangle t1(x1, y1, z1), t2(x2, y2, z2);
	SumArea(t1, t2);
}