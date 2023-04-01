import java.util.*;

public class Hello {
  public static void main(String[] args){
    new Hello();
  } // end main

  public Hello(){
    String name;
    Scanner input = new Scanner(System.in);
    System.out.print("Hi, what is your name? ");
    name = input.nextLine();
    System.out.println("Hello " +  name + " from Java");
  } // end constructor
} // end class

