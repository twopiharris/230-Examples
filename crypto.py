import java.util.Random;
import java.util.Scanner;

public class Crypto {

  static Scanner input = new Scanner(System.in);
  static String alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
  static String key = "UBWKOVGAPRFJLCQHZENSXDMYTI";
    
  public static void main(String[] args) {
    boolean keepGoing = true;
    while(keepGoing){

      String response = menu();

        if (response.equals("1")){
          System.out.println("Please enter unencrypted phrase");
          String plain = input.nextLine();
          plain = plain.toUpperCase();
          System.out.println(encrypt(plain));

        } else if (response.equals("2")){
          System.out.println("Please enter encrypted phrase");
          String code = input.nextLine();
          code = code.toUpperCase();
          System.out.println(decrypt(code));

        } else if (response.equals("0")){
          System.out.println("Goodbye!");
          keepGoing = false;

        } else {
          System.out.println("Sorry. I didn't understand");
        } // end if
      } // end while
   } // end main    
} // end Crypto
