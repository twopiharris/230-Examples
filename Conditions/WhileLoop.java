/*
 * WhileLoop.java
 *
 * Created on January 28, 2007, 9:44 PM
 *
 * To change this template, choose Tools | Template Manager
 * and open the template in the editor.
 */

/**
 *
 * @author aharris
 */
import java.util.*;

public class WhileLoop {
    
    public static void main(String args[]){
      new WhileLoop();
    } // end main

    public WhileLoop(){
        String guess = "";
        String correct = "1776";
        Scanner input = new Scanner(System.in);
        while (!guess.equals(correct)){
            System.out.println("What year was the U.S. Declaration of Independence signed? ");
            guess = input.next();
        } // end while
        System.out.println("Good job!");
 
    } // end constructor
}
