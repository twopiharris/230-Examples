// Use this class to test your own Rectangle class

public class RecDemo {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// You can't substantially change this code.
		// Write your Rectangle class so the following
		// code will work correctly.
		
		Rectangle myRec;
		
		myRec = new Rectangle(5d, 3d);
		System.out.println(myRec.getValues());
		
		myRec = new Rectangle();
		System.out.println(myRec.getValues());
		
		myRec = new Rectangle(Rectangle.SMALL);
		System.out.println(myRec.getValues());
		
		myRec = new Rectangle(Rectangle.MEDIUM);
		System.out.println(myRec.getValues());
		
		myRec = new Rectangle(Rectangle.LARGE);
		System.out.println(myRec.getValues());

		System.out.println(Rectangle.calcPerimeter(5d, 6d));
		System.out.println(Rectangle.calcArea(5d, 6d));
		
	} // end main

} // end RecDemo

class Rectangle {
	private double width;
	private double height;
	private double area;
	private double perimeter;
	
	//constants
	public final static int SMALL = 1;
	public final static int MEDIUM = 2;
	public final static int LARGE = 3;
	
	//Standard 2 double constructor
	public Rectangle(double iWidth, double iHeight){
		width = iWidth;
		height = iHeight;
		area = this.getArea();
		perimeter = this.getPerimeter();
	} // end 2 double constructor
	
	//No parameter constructor
	public Rectangle(){
		this(5d, 10d);
	} // end no param
	
	//single int constructor
	public Rectangle(int size){
		if (size == 1){
			width = 2d;
			height = 3d;
		} else if (size == 2){
			width = 5d;
			height = 10d;
		} else if (size == 3){
			width = 10d;
			height = 15d;
		} else {
			// invalid input. Go small
			width = 2d;
			height = 3d;
		} // end if
		area = this.getArea();
		perimeter = this.getPerimeter();
	} // end single int constructor
	
	public double getArea(){
		return width * height;
	} // end getArea
	
	public double getPerimeter(){
		return 2 * (width + height);
	} // end getPerimeter

	public String getValues(){
		String output = "";
		output += "width: " + width;
		output += ", height: " + height;
		output += ", area: " + area;
		output += ", perimeter: " + perimeter;
		return output;
	} // end getValues
	
	public static double calcPerimeter(double width, double height){
		return 2 * (width + height);
	} // end calcPerimeter
	
	public static double calcArea(double width, double height){
		return width * height;
	} // end calcArea
	
} // end class
