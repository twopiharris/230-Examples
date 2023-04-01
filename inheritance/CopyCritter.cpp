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


//Constructor and greet are defined for Critter
Critter::Critter(string name){
  Critter::name = name;
};

void Critter::greet(){
  cout << "My name is " << name << "." << endl;
} // end greet

//note that copyCritter is derived from Critter
class CopyCritter: public Critter{};
//NOTHING is defined for CopyCritter!

int main(){

  cout << "main class: ";
  Critter c;
  c.greet();


  //CopyCritter doesn't have an explicit constructor
  //or greet, but it derives them both from its parent

  cout << "derived class: ";
  CopyCritter cc;
  cc.greet();

  return 0;
}

