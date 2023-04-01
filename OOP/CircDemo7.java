// adding private instance variables

public class CircDemo7 {
    
  public static void main(String args[]){
      Circle7 myCirc = new Circle7();
      System.out.println(myCirc.getRadius());
  }    
} // end class def

class Circle7 {
    
    // instance variable is now private / protected
    // only access is through getter / setter methods
    protected float radius;
    
    public Circle7(float localRad){
        this.radius = localRad;
    } // end constructor
    
    public Circle7(int localRad){
        this.radius = (float)localRad;
    } // end constructor
    
    public Circle7(){
        this.radius = 10f;
    } // end constructor
    
    public void setRadius(float localRad){
        this.radius = localRad;
    } // end setRadius
    
    public void setRadius(int localRad){
        this.radius = (float)localRad;
    } // end setRadius
    
    public float getRadius(){
        return this.radius;
    } // end getRadius
    
    public String getRadiusString(){
        return String.valueOf(this.radius);
    } // end getRadiusString
} // end Circle7 class def
