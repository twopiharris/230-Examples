// be sure we can do input and output
#include <stdio.h>

int main(){
  // set aside memory called userName
  char userName[20];
  //Ask user name
  printf("What is your name? ");
  //put input into userName
  scanf("%s", userName);
  //print greeting incorporating userName
  printf("Hi there, %s! \n", userName);
  return(0);
} // end main

