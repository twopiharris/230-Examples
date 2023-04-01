/*
 * RollDice.java
 *
 * Created on January 28, 2007, 9:05 PM
 *
 * Demo rolling a six-sided die
 */

/**
 *
 * @author aharris
 */

import java.util.*;
        
public class RollDice {
    
    public static void main(String args[]){
      new RollDice();
    } // end main

    public RollDice(){
        Random generator = new Random();
      
        int die = generator.nextInt(6);
        die += 1;
        System.out.println(die);

        //Alternate form using Math.random();
        double roll = Math.random();
        roll *= 6;
        die = (int)roll + 1;
        System.out.println(die);
      
    }

    
}
