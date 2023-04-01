//mapDemo

#include <map>
#include <iostream>

using namespace std;

int main(){
  map<string, string> stateCap;
  stateCap["Indiana"] = "Indianapolis";
  stateCap["Florida"] = "Tallahasee";

  cout << stateCap["Indiana"] << endl;

  return 0;
} // end main



