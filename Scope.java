public class Scope {

    public static int classLevel = 1;

    public static void main(String[] args){
	int inMain = 2;
        System.out.println("In main, classlevel: " + classLevel);
	System.out.println("In main, inMain: " + inMain);
	//System.out.println("In main, inSecond: " + inSecond);

	second();
    } // end main

    public static void second(){
	int inSecond = 3;
        System.out.println("In second, classlevel: " + classLevel);
	//System.out.println("In second, inMain: " + inMain);
	System.out.println("In second, inSecond: " + inSecond);
    } // end second
} // end class def

	