#include <string>

//Critter.h
class Critter{
  protected:
    string name;
  public:
    Critter(string name = "anonymous");
    void greet();
}; // end Critter def
