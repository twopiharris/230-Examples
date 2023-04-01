/*
 * IfAce.java
 *
 * Created on January 28, 2007, 9:17 PM
 *
 * Demo basic if statement
 */

/**
 *
 * @author aharris
 */

import java.util.*;
public class IfAce {
    
    public static void main(String args[]){
      new IfAce();
    } // end main

    public IfAce(){
        Random generator = new Random();
        int die = generator.nextInt(6) + 1;
        System.out.println(die);
        if (die == 1){
            System.out.println("It's an ACE!!!");
        } // end if

    } // end constructor
    
} // end class
