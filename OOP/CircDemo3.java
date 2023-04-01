public class CircDemo3 {
    public static void main(String args[]){
        //test single float constructor
        Circle3 myCirc = new Circle3(5.6f);
        System.out.println("Single float: " + myCirc.radius);
        
        //test single int constructor
        myCirc = new Circle3(5);
        System.out.println("Single int: " + myCirc.radius);
        
        //test no param constructor
        myCirc = new Circle3();
        System.out.printf("No parameter: %.2f\n", 
        		           new Object[]{ 
        		             new Float(myCirc.radius)} );
        
    } // end main  
} // end CircDemo3

class Circle3 {
    float radius;
    
    public Circle3(float localRad){
        radius = localRad;
    } // end float constructor
    
    public Circle3(int localRad){
        radius = (float)localRad;
    } // end int constructor
    
    public Circle3(){
        radius = 10f;
    } // end no param constructor
} // end class def