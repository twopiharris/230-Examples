#include <iostream>

using namespace std;

class Critter {
  private:
    string name;
  public:
    Critter(string name);
    void setName(string name);
    string getName();
    string greet();
};

Critter::Critter(string name = "Anonymous"){
  Critter::name = name;
} // end constructor

void Critter::setName(string name){
  Critter::name = name;
} // end setName

string Critter::getName(){
  return Critter::name;
} // end getName

string Critter::greet(){
  return "Hi, my name is " + Critter::name;
} // end greet

int main(){
  Critter c;
  c.setName("George");
  cout << c.greet() << endl;
}
