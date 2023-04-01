/*
 * HiBill.java
 *
 * Created on January 10, 2007, 12:44 PM
 *
 * Checks to see if Bill Gates is running the program
 * Checks to see if the user is Bill Gates. Uses Scanner.nextLine and
 * if - else construct
 */

/**
 *
 * @author aharris
 */

import java.util.Scanner;

public class HiBill {
    
    public static void main(String args[]){
        new HiBill();
    } // end main

    public HiBill(){
        Scanner input = new Scanner(System.in);
        System.out.println("What is your name? ");
        String userName = input.nextLine();
        
        if (userName.equals("Bill Gates")){
            System.out.println("Why are you using Java?");
        } else {
            System.out.println("Nice to meet you, " + userName);
        } // end if

        //Equality operator appears to work, but not as expected
        if (userName == "Bill Gates"){
            System.out.println("They are the same memory");
        } else {
            System.out.println("They are different memory");
        } // end if

    } // end constructor
} // end HiBill class def
 
