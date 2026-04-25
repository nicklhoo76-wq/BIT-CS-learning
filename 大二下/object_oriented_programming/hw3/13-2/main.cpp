#include "counted.h"
using namespace std;
int main() {
	Counted *c = new Counted;
	delete c;
	Counted *array = new Counted[5];
	delete[] array;
}