import java.util.*;
public class KeepGoing {
    public static void main(String[] args){
      new KeepGoing();
    } // end main

    public KeepGoing(){
	Scanner input = new Scanner(System.in);
	String response;
	String CORRECT = "Keiser";
	int tries = 0;
	boolean keepGoing = true;

        while(keepGoing){
            tries++;
	    System.out.print(tries + ") What is the password? ");
	    response = input.nextLine();
	    if (response.equals(CORRECT)){
		System.out.println("Correct");
		keepGoing = false;
            } else {

		if (tries >= 3){
		    System.out.println("Too many tries. Launching missiles.");
		    keepGoing = false;
		} // end 'tries' if
	    } // end 'correct' if
	} // end while

    } // end constructor

} // end class def
