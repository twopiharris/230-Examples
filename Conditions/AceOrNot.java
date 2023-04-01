/*
 * AceOrNot.java
 *
 * Created on January 28, 2007, 9:22 PM
 *
 * Demo if-else
 */

/**
 *
 * @author aharris
 */
import java.util.*;

public class AceOrNot {
    public static void main(String args[]){
      new AceOrNot();
    } // end main

    public AceOrNot(){
        Random generator = new Random();
        int die = generator.nextInt(6)+1;
        if (die == 1){
            System.out.println("It's an ACE!");
        } else {
            System.out.println("It's only a " + die);
        } // end if

    } // end constructor

} // end class def
