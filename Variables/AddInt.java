/*
 * AddInt.java
 *
 * Created on January 10, 2007, 12:51 PM
 *
 * Accepts two integers and adds them up. Note errors if you enter
 * floats or strings
 */

/**
 *
 * @author aharris
 */
import java.util.Scanner;

public class AddInt {
    
    public static void main(String args[]){
        new AddInt();
    } // end main

    public AddInt(){
        Scanner input = new Scanner(System.in);
        System.out.println("Please give me a number");
        int x = input.nextInt();
        System.out.println("Please give me another number");
        int y = input.nextInt();
        int sum = x + y;
        
        System.out.println("The sum is " + sum);
    } // end constructor

} // end class def
