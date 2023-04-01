import java.util.*;

public class ByVal{
    public static void main(String[] args){
	int regInt = 5;
        int[] wrappedInt = new int[1];
	wrappedInt[0] = 5;

	addVals(regInt, wrappedInt);

	System.out.println("after function: reg: " + regInt + ", wrapped: " + wrappedInt[0]);
    } // end main

    public static void addVals(int regInt, int[] wrappedInt){
	regInt++;

	wrappedInt[0]++;
	System.out.println("Inside - reg: " + regInt + ", wrapped: " + wrappedInt[0]);
    } // end addVals
} // end class def
