// adding setters

public class CircDemo4 {
    
    public static void main(String args[]){
        
        Circle4 myCirc = new Circle4();
        System.out.println("default radius: " + myCirc.radius);

        //change radius with float method
        myCirc.setRadius(7.3f);
        System.out.println("float radius: " + myCirc.radius);

        //change radius with int method
        myCirc.setRadius(4);
        System.out.println("int radius: " + myCirc.radius);

    } // end main
} // end CircDemo4

class Circle4 {
    float radius;
    
    public Circle4(float localRad){
        radius = localRad;
    } // end constructor
    
    public Circle4(int localRad){
        radius = (float)localRad;
    } // end constructor
    
    public Circle4(){
        radius = 10f;
    } // end constructor
    
    public void setRadius(float localRad){
        radius = localRad;
    } // end setRadius
    
    public void setRadius(int localRad){
        radius = (float)localRad;
    } // end setRadius
    
} // end Circle4