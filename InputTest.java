//InputTest.java
//Shows how to use the scanner class and a variable for input

import java.util.Scanner;

class InputTest {

    public static void main(String[] args){
	Scanner input = new Scanner(System.in);
        System.out.println("What is your name?");
        String userName = input.nextLine();
        System.out.println("Hi there, " + userName + "!");
    } // end main
} // end class def

/* 

Notes:

   Import the Scanner class from java utility package
   Create an instance called input.
   Scanner needs to know where input will be coming from (file, console)
   System.in refers to console
   String is a text variable.
   input.next returns the next String token (usually a word)
   Plus sign is overloaded - in this case it's concatenating, not adding
*/
