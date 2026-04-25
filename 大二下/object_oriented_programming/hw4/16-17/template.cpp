#include<iostream>
using namespace std;

template< typename T >
class Data {
	T i;
public:
	Data(T ii) : i(ii) {
		cout << ">" << i << ' ';
	}
	~Data() {
		cout << "~" << i << ' ';
	}
	operator T() const { return i; }
	friend ostream& operator<<(ostream& os, const Data& x) {
		return os << "Data: " << x.i;
	}
	friend ostream& operator<<(ostream& os, const Data* x) {
		return os << "Data: " << x->i;
	}
};