// assumes Circle7 and Circle8 defined in same project

public class CircDemo9 {
  public static void main(String args[]){
	  //creating an array of objects
	  
	  //the ARRAY is an object
	  //first new statement initializes the array
	  Circle8[] allTheCircles = new Circle8[10];
	  
	  //however, the circles inside the array
	  //have not yet been created. They are null
	  
	  System.out.println(allTheCircles[0]);
	  //System.out.println(allTheCircles[0].getCircumference());
	  
	  //you must instantiate all elements with a loop
	  for (int i = 0; i < allTheCircles.length; i++){
		  allTheCircles[i] = new Circle8(5f);
	  } // end for
	  
	  //now this works.
	  System.out.println(allTheCircles[0].getCircumference());
  
  }  // end main 
} // end class def

