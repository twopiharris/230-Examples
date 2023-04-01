// adding getter methods. It's now a java bean!

public class CircDemo5 {
    public static void main(String args[]){
        
        Circle5 myCirc = new Circle5();
        System.out.println("default radius: " + myCirc.radius);

        //change radius with float method
        myCirc.setRadius(7.3f);
        System.out.println("getting radius: " + myCirc.getRadius());

        //change radius with int method
        myCirc.setRadius(4);
        System.out.println("string radius: " + myCirc.getRadiusString());
    } // end main
} // end class def
    

class Circle5 {
    float radius;
    
    public Circle5(float localRad){
        radius = localRad;
    } // end constructor
    
    public Circle5(int localRad){
        radius = (float)localRad;
    } // end constructor
    
    public Circle5(){
        radius = 10f;
    } // end constructor
    
    public void setRadius(float localRad){
        radius = localRad;
    } // end setRadius
    
    public void setRadius(int localRad){
        radius = (float)localRad;
    } // end setRadius
    
    public float getRadius(){
        return radius;
    } // end getRadius
    
    public String getRadiusString(){
        return String.valueOf(radius);
    } // end getRadiusString
} // end Circle5 class def