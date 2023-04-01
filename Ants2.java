
public class Ants2 {

	/**
	 * Ants2.java
	 * Now the methods take parameters and return results
	 * 
	 */
	
	public static void main(String[] args) {
		System.out.println(verse(1));
		System.out.println(chorus());
		System.out.println(verse(2));
		System.out.println(chorus());
	} // end main
	
	public static String chorus(){
	    String result = " \n";
		result += "...and they all go marching \n";
		result += "down \n";
		result += "to the ground \n";
		result += "to get out \n";
		result += "of the rain \n";
		result += "Boom boom boom boom boom boom boom boom \n";
		result += " \n";
		return result;
	} // end chorus
	
	public static String verse(int verseNum){
	    String result = "";
	    String distraction = "";
	    
	    //determine the distraction
	    switch (verseNum){
	    	case 1:
	    		distraction = "suck his thumb";
	    		break;
	    	case 2:
	    		distraction = "tie his shoe";
	    		break;
	    	default:
	    		distraction = "I have no idea...";
	    } // end switch
	    
	    //create the verse

	    result += "The ants go marching " + verseNum;
		result += " by " + verseNum + " hurrah, hurrah... \n";
		
	    result += "The ants go marching " + verseNum;
		result += " by " + verseNum + " hurrah, hurrah... \n";
		
	    result += "The little one stops to " + distraction + " \n";
		result += " \n";
		return result;

	} // end verse

} // end class def
