#include <string>
#include <iostream>

using namespace std;

//CopyCritter
class Critter{
  protected:
    string name;
  public:
    Critter(string name = "anonymous");
    void greet();
}; // end Critter def

//note that copyCritter is derived from Critter
class BitterCritter: public Critter{
  public:
    void greet();
};

//Constructor and greet are defined for Critter
Critter::Critter(string name){
  Critter::name = name;
};

void Critter::greet(){
  cout << "My name is " << name << "." << endl;
} // end greet

void BitterCritter::greet(){
  //use scope res operator (::) to access parent members
  Critter::greet();
  cout << "...as if you care..." << endl;
}

int main(){

  cout << "main class: ";
  Critter c;
  c.greet();


//BitterCritter
  cout << "derived class: ";
  BitterCritter bc;
  bc.greet();

  return 0;
}

