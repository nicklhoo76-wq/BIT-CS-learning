#pragma once
#include<iostream>
#include<string>
class Employee {
public:
	std::string name;
	double salary;
	Employee(std::string n) :name(n),salary(0) {}
	virtual void pay() = 0;
};

class Manager : virtual public Employee {
public:
	Manager(std::string n) :Employee(n) {}
	virtual void pay();
};

class Technician : virtual public Employee {
	float worktime;
public:
	Technician(std::string n, float time):Employee(n), worktime(time){}
	virtual void pay();
};

class Salesman : virtual public Employee {
	int sale;
public:
	Salesman(std::string n, int s):Employee(n), sale(s){}
	virtual void pay();
};

class SalesManager : virtual public Manager, Salesman {
	int sale;
public:
	SalesManager(std::string n, int s):Employee(n), Manager(n), Salesman(n, s), sale(s){}
	virtual void pay();
};