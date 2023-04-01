import java.util.*;

public class Hello {
  public Hello(){
    String name;
    Scanner input = new Scanner(System.in);
    System.out.println("Hi. What is your name? ");
    name = input.nextLine();
    System.out.println("Hello " + name + " from Java");
  } // end constructor

  public static void main(String[] args){
    new Hello();
  } // end main
} // end class def

