#include<iostream>
#include"mammal.h"
void Mammal::Speak() {
	std::cout << "I'm a mammal." << std::endl;
}
void Dog::Speak() {
	std::cout << "I'm a dog." << std::endl;
}
void Pug::Speak() {
	std::cout << "I'm a pug." << std::endl;
}

void Talk(Mammal& m) {
	m.Speak();
}