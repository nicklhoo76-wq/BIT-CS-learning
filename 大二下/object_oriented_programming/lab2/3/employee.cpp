#include"employee.h"
#include<iostream>
void Manager::pay() {
	salary = 7000;
	std::cout << "manager " << name << "'s salary is "  << salary << std::endl;
}
void Technician::pay() {
	salary = 100 * worktime;
	std::cout << "technician " << name << "'s salary is " << salary << std::endl;
}
void Salesman::pay() {
	salary = sale * 0.05;
	std::cout << "salesman " << name << "'s salary is " << salary << std::endl;
}
void SalesManager::pay() {
	salary = 4000 + sale * 0.005;
	std::cout << "salesmanager " << name << "'s salary is " << salary << std::endl;
}