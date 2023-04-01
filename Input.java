//Input.java
//Shows how to use the scanner class and a variable for input

import java.util.Scanner;

class Input {

    public static void main(String[] args){
	Scanner input = new Scanner(System.in);
        System.out.println("What is your name?");
        String userName = input.next();
        System.out.println("Hi there, " + userName + "!");
    } // end main
} // end class def

