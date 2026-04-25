#include<iostream>
#include"employee.h"
int main() {
	Technician t("technician1", 150.5);
	Manager m(":manager1");
	Salesman s("salesman1", 200000);
	SalesManager sm("salesmanager1", 500000);
	t.pay();
	m.pay();
	s.pay();
	sm.pay();
}