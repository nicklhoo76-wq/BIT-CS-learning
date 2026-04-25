#pragma once
class Mammal {
public:
	virtual void Speak();
};

class Dog :public Mammal {
public:
	virtual void Speak();
};

class Pug : public Dog {
public:
	virtual void Speak();
};

void Talk(Mammal& m);