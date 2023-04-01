import java.io.*;
public class SerialDemo {

	
	public static void main(String[] args) {
		new SerialDemo();
	} // end main
	
	public SerialDemo(){
		saveCritter();
		loadCritter();
		
	} // end constructor
	
	public void saveCritter(){
		Critter myCritter = new Critter("Lizzie Borden", 1);
		try {
			FileOutputStream fo = new FileOutputStream("SerialCritter.txt");
			ObjectOutputStream obOut = new ObjectOutputStream(fo);
			obOut.writeObject(myCritter);
		} catch (Exception e){
			System.out.println(e.getMessage());
		} // end try
	} // end saveCritter
	
    public void loadCritter(){
    	Critter myCritter;
    	try {
    		FileInputStream fIn = new FileInputStream("SerialCritter.txt");
    		ObjectInputStream obIn = new ObjectInputStream(fIn);
    		myCritter = (Critter)obIn.readObject();
        	System.out.println(myCritter.name);
    	}catch (Exception e){
    		System.out.println(e.getMessage());
    	} // end try
    } // end loadCritter

} // end class def

class Critter implements Serializable{
	String name;
	int age;
	
	public Critter(String lName, int lAge){
		name = lName;
		age = lAge;
	} // end constructor
} // end class def