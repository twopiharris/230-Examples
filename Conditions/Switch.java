/*
 * Switch.java
 *
 * Created on January 28, 2007, 9:30 PM
 *
 * Demo java switch
 */

/**
 *
 * @author aharris
 */
import java.util.*;
public class Switch {
    public static void main(String args[]){
      new Switch();
    } // end main

    public Switch(){
        Random generator = new Random();
        int die = generator.nextInt(6)+1;
        String result = "";
        //note that switches DO NOT WORK on Strings!!
        switch(die){
            case 1:
                result = "0001";
                break;
            case 2:
                result = "0010";
                break;
            case 3:
                result = "0011";
                break;
            case 4:
                result = "0100";
                break;
            case 5:
                result = "0101";
                break;
            case 6:
                result = "0110";
                break;
            default:
                result = "PROBLEM!!!";
                break;
        } // end switch
        System.out.println(result);

    } // end constructor
    
}
