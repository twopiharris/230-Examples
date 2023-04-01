//vectorDemo

#include <vector>
#include <iostream>

using namespace std;
int main(){

  //you don't need to specify the length of a vector!
  //however, you do need to specify the type
  vector<int> a;

  //use push_back to add an element to the end of a vector
  a.push_back(1);
  a.push_back(2);
  a.push_back(3);

  //You can access a vector
  cout << a[2] << endl;

  //remove an element with pop_back
  a.pop_back();

  //insert to add an element to an arbitrary spot
  //use begin() and end() to get key positions
  a.insert(a.end(), 300);
  a.insert(a.begin() + 1, 4);
  //inserting an element moves later elements

  cout << a[2] << endl << endl;

  //iterating through the vector
  vector<int>::iterator it;
  for(it = a.begin(); it < a.end(); it++){
    cout << *it << endl;
  } // end for loop

  return 0;
} // end main

