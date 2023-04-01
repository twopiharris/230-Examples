//Hello.java

import java.util.*;

public class Hello {
    public static void main (String[] args){
      Scanner input = new Scanner(System.in);
      String userName;
      System.out.println("What is your name?");
      userName = input.nextLine();
      System.out.println("Hi there, " + userName + "!");
    } // end main
} 
