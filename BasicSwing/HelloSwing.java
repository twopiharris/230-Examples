/*
 * HelloSwing.java
 *
 * Created on February 12, 2007, 1:06 PM
 *
 * Simple GUI demo
 */

/**
 *
 * @author aharris
 */

import javax.swing.*;

public class HelloSwing extends JFrame{
    
    public static void main(String args[]){
        new HelloSwing();
    } // end main
    
    /** Creates a new instance of HelloSwing */
    public HelloSwing() {
        super("Hello, world!");
        this.setDefaultCloseOperation(HelloSwing.EXIT_ON_CLOSE);
        java.awt.Container surface = this.getContentPane();
        surface.add(new JLabel("Hello, world!"));
        this.pack();
        this.setVisible(true);
    } // end constructor
    
} // end class def