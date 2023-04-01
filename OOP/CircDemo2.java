// Adding a Constructor

public class CircDemo2 {

    public static void main(String args[]){
        //set the radius with the constructor
        Circle2 myCirc = new Circle2(3.1f);
        System.out.println(myCirc.radius);
        
        //change the radius and check it
        myCirc.radius = 4.5f;
        System.out.println(myCirc.radius);
        
    } // end main
} // end class def

class Circle2 {
    float radius;
    
    public Circle2 (float localRad){
        radius = localRad;
    } // end constructor
} // end Circle2 def