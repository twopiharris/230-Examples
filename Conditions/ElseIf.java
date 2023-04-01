/*
 * ElseIf.java
 *
 * Created on January 28, 2007, 9:26 PM
 * demo if-elsif
 */

/**
 *
 * @author aharris
 */
import java.util.*;

public class ElseIf {

    public static void main(String args[]){
      new ElseIf();
    } // end main

    public ElseIf(){
        Random generator = new Random();
        int die = generator.nextInt(6) + 1;
        if (die == 1){
            System.out.println("I");
        } else if (die == 2){
            System.out.println("II");
        } else if (die == 3){
            System.out.println("III");
        } else if (die == 4){
            System.out.println("IV");
        } else if (die == 5){
            System.out.println("V");
        } else if (die == 6){
            System.out.println("VI");
        } else {
            System.out.println("Something went wrong...");
        } // end if

    } // end constructor

} // end class
