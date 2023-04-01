// Changer.java
// Basic Changemaker lab

import java.util.*;

public class Changer{
  public static void main(String[] args){
    new Changer();
  } // end mian

  public Changer(){
    Scanner input = new Scanner(System.in);
    float itemCost;
    float tendered;
    float changeDue;
    int penniesLeft;

    System.out.println("How much does the item cost? ");
    itemCost = input.nextFloat();

    System.out.println("How much was paid? ");
    tendered = input.nextFloat();

    changeDue = tendered - itemCost;
    System.out.println("Change Due: " + changeDue);

    penniesLeft = (int)(tendered * 100) - (int)(itemCost * 100);
    System.out.println("PenniesLeft: " + penniesLeft);

    int twenties = (int)(penniesLeft / 2000);
    penniesLeft = penniesLeft % 2000;
    System.out.println("Twenties: " + twenties);

    int tens = (int)(penniesLeft / 1000);
    penniesLeft = penniesLeft % 1000;
    System.out.println("Tens: " + tens);
    
    int fives = (int)(penniesLeft / 500);
    penniesLeft = penniesLeft % 500;
    System.out.println("Fives: " + fives);

    int ones = (int)(penniesLeft / 100);
    penniesLeft = penniesLeft % 100;
    System.out.println("Ones: " + ones);

    int quarters = (int)(penniesLeft / 25);
    penniesLeft = penniesLeft % 25;
    System.out.println("Quarters: " + quarters);

    int dimes = (int)(penniesLeft / 10);
    penniesLeft = penniesLeft % 10;
    System.out.println("Dimes: " + dimes);

    int nickels = (int)(penniesLeft / 5);
    penniesLeft = penniesLeft % 5;
    System.out.println("Nickels: " + nickels);

    System.out.println("Pennies: " + penniesLeft);

  } // end constructor
} // end class def


    
