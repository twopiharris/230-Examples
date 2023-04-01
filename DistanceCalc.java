import java.util.*;
public class DistanceCalc {

	/**
	 * @param args
	 */
	
	static String[] city = {
		"Indianapolis",
		"New York",
		"Tokyo",
		"London",
	};

	static int[][] distance = {
		{0, 648, 6476, 4000},
		{648, 0, 6760, 3470},
		{6476, 6760, 0, 956},
		{4000, 3470, 5956, 0}
	};
		
	public static void main(String[] args) {
		boolean keepGoing = true;
    	Scanner input = new Scanner(System.in);

    	while (keepGoing){
			int from = getCity("origin");
			int to = getCity("destination");
			int result = 0;
			result = distance[from][to];
		
			System.out.print("The distance between ");
			System.out.print(city[from]);
			System.out.print(" and ");
			System.out.print(city[to]);
			System.out.print(" is ");
			System.out.print(result);
			System.out.println(" miles.");
			
			// see if they want to play again
			System.out.println("");
			System.out.println("Try again? (Y/N)");
			String tryAgain = input.nextLine();
			tryAgain = tryAgain.toUpperCase();
			char firstChar = tryAgain.charAt(0);
			
			if (firstChar == 'Y'){
				keepGoing = true;
			} else {
				keepGoing = false;
			} // end if
		
		} // end while
		
	} // end main

    public static int getCity(String prompt){
    	Scanner input = new Scanner(System.in);
    	int result = 0;
    	
    	System.out.println(prompt);
    	System.out.println("");
    	System.out.println("0) Indianapolis");
    	System.out.println("1) New York");
    	System.out.println("2) Tokyo");
    	System.out.println("3) London");
    	System.out.println("");
    	System.out.println("Please select a city number");
    	//catch alpha input
    	try {
    		result = Integer.parseInt(input.nextLine());
    	} catch (Exception e){
    		System.out.println("Something went wrong...");
    		System.out.println("Assuming city 0");
    		result = 0;
    	} // end try
    	
    	//catch out of range input
    	if ((result >= city.length) || (result < 0)){
    		System.out.println("Incorrect input. Assuming 0");
    		result = 0;
    	} // end if
    	return result;
    } // end getCity
} // end clasDef

