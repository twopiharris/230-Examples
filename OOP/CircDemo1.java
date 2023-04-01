// Creating a basic circle

public class CircDemo1 {
    public static void main(String args[]){
        Circle1 myCirc = new Circle1();
        myCirc.radius = 1.0f;
        System.out.println(myCirc.radius);
    } // end main
    
} // end cirDemo1

class Circle1 {
    float radius;
}
