//Demonstrate how to convert between various types
import java.util.*;

public class Convert {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		
		System.out.println("Please enter a number");
		String rawData = input.nextLine();
		float myFloat = Float.parseFloat(rawData);
		System.out.println("The floating point value is " + myFloat);
		
		int myInt = Integer.parseInt(rawData);
		System.out.println("The integer value is " + myInt);
		System.out.print("I'll square it and return a string: ");
		System.out.println(String.valueOf(myInt * myInt));
		System.out.print("Here's the number in Hexadecimal: ");
		System.out.println(Integer.toHexString(myInt));
		int result = (int)5.7 + (int)3.9;
		System.out.println(result);
	}

}
