/*
 * ForLoops.java
 *
 * Created on January 28, 2007, 9:37 PM
 * Demo For loops
 */

/**
 *
 * @author aharris
 */


public class ForLoops {
    public static void main(String args[]){
      new ForLoops();
    } // end main

    public ForLoops(){
        int counter = 0;
        
        System.out.println("Ordinary for loop");
        for (counter = 0; counter <= 10; counter++){
            System.out.println(counter);
        } // end for loop
        
        System.out.println("Counting backwards");
        for (counter = 10; counter > 0; counter--){
            System.out.println(counter);
        } // end for loop
        
        System.out.println("Counting by 5");
        for (counter =0; counter <= 25; counter += 5){
            System.out.println(counter);
        } // end for loop

    } // end constructor
    
} // end class def
