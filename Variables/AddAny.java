/*
 * AddAny.java
 *
 * Created on January 10, 2007, 1:01 PM
 *
 * Take any type of input and try to add it up
 * Take input as a string, attempt to convert it to a float, 
 * and if you can't, tell the user and make it 0f.
 * Introduces Float object and exception-handling.
 */

/**
 *
 * @author aharris
 */
import java.util.Scanner;

public class AddAny {
    public static void main(String args[]){
        Scanner input = new Scanner(System.in);
        float x;
        float y;
        
        System.out.println("First number: ");
        String xRaw = input.nextLine();
        
        try {
            x = Float.parseFloat(xRaw);
        } catch(NumberFormatException e){ 
            System.out.println("ERROR: Using 0 instead...");
            System.out.println(e.getMessage());
            x = 0f;
        }
        
        System.out.println("Second number: ");
        String yRaw = input.next();
        try {
            y = Float.parseFloat(yRaw);
        } catch (NumberFormatException e){
            System.out.println("ERROR: Using 0 instead...");
            y = 0f;
        }
        
        float sum = x + y;
        System.out.println("The sum is " + sum);
        
    } // end main
    
} // end class def