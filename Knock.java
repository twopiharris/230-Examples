// Knock.java
// Basic Knock-knock joke

import java.util.Scanner;

class Knock {
    public static void main(String[] args){
	Scanner input = new Scanner(System.in);
        String dummy = new String();
        String userName = new String();
        
        System.out.println("What is your name?");
        userName = input.next();

        System.out.println("Nice to meet you, " + userName + "!");
        System.out.println("Knock Knock");

	dummy = input.nextLine();
        System.out.println("Cargo");
	dummy = input.nextLine();
        System.out.println("Cargo Beep beep");
        System.out.println("I crack myself up, " + userName + "!");
    } // end main
} // end class def

