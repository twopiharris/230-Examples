/*
 * HiUser.java
 *
 * Created on February 12, 2007, 1:16 PM
 *
 * Demo basic GUI setup, Grid Manager, buttons
 */

/**
 *
 * @author aharris
 */
import java.awt.*;
import javax.swing.*;
public class HiUser extends JFrame{
   // instance vars
    JLabel output = new JLabel("Output");
    JButton clickMe = new JButton("Click me");
    JTextField input = new JTextField("Input");
    
    public static void main(String args[]){
        new HiUser();
    } // end main
    
    /** Creates a new instance of HiUser */
    public HiUser() {
        super("Hi, user");
        Container surface = this.getContentPane();
        surface.setLayout(new GridLayout(3,1));
        surface.add(output);
        surface.add(clickMe);
        surface.add(input);
        this.pack();
        this.setVisible(true);
    } // end constructor
} // end class def
