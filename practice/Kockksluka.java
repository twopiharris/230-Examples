//Knockksluka.java
//Knock knock joke
//Kristi Sluka

import java.util.Scanner;

class Knockksluka {

    public static void main(String[] args){
        Scanner knock = new Scanner(System.in);
        System.out.println("Hello! What's your name?");
        String userName = knock.nextLine();
        System.out.println("Here's a joke, " + userName + ":");
        System.out.println("Knock knock");
        String first = knock.next();
        System.out.println("Candace");
        String second = knock.next();
        System.out.println("Candace be the last knock knock joke?");


    }//end main

}//end class def 