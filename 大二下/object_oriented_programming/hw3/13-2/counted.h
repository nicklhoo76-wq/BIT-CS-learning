#pragma once
#include<iostream>
class Counted {
	int id;
	static int count;
public:
	Counted() :id(count++) {
		std::cout << "id:" << id << '\n' << "created." << std::endl;
	}
	~Counted() {
		std::cout << "destroyed." << std::endl;
	}
};

int Counted::count = 0;