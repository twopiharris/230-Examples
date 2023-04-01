#include <string>
#include <iostream>

#include "Critter.h"

using namespace std;

//Constructor and greet are defined for Critter
Critter::Critter(string name){
  Critter::name = name;
};

void Critter::greet(){
  cout << "My name is " << name << "." << endl;
} // end greet

int main(){

  cout << "main class: ";
  Critter c;
  c.greet();

  return 0;
}

