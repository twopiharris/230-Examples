/*
 * addFloat.java
 *
 * Created on January 10, 2007, 12:56 PM
 *
 * This time input floating point numbers, and add them up
 * Can handle integers or floats, but still not strings.
 */

/**
 *
 * @author aharris
 */

import java.util.Scanner;

public class AddFloat {

    public static void main(String args[]){
        Scanner input = new Scanner(System.in);
        System.out.println("First number: ");
        float x = input.nextFloat();
        System.out.println("Second number: ");
        float y = input.nextFloat();
        float sum = x + y;
        System.out.println(4 + 5.5);
        System.out.println("The sum is " + sum);
        
    } // end main
    
} // end class def