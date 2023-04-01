
public class Ants3 {

	/**
	 * Ants3.java
	 * Arrays are cool
	 * 
	 */
	
	public static String[] distractionList = 
	  {"", "suck his thumb", "tie his shoe", "climb a tree"};
	
	public static void main(String[] args) {
	//Hi there, this is a comment	
		for (int i = 1; i < distractionList.length; i++){
			System.out.println(verse(i));
			System.out.println(chorus());
		}
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
	    String distraction = distractionList[verseNum];
	    
	    result += "The ants go marching " + verseNum;
		result += " by " + verseNum + " hurrah, hurrah... \n";
		
	    result += "The ants go marching " + verseNum;
		result += " by " + verseNum + " hurrah, hurrah... \n";
		
	    result += "The little one stops to " + distraction + " \n";
		result += " \n";
		return result;

	} // end verse

} // end class def
