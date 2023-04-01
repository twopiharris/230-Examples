import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

public class ShowImage extends JFrame {
  ImageIcon ball;
 
  public static void main(String args[]){
	  new ShowImage();
  } // end main
  
  public ShowImage(){
	  super("Display an Image");
	  //load up the image
	  ball = new ImageIcon("ball.gif");

	  this.setSize(400, 400);
	  this.setVisible(true);
	  this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	  
  } // end constructor
  
  public void paint(Graphics g) {
	  super.paint(g);
	  g.drawImage(ball.getImage(), 100, 100, null);
	  //g.drawRect(0, 0, 100, 100);
  } // end paint
  
  
} // end class def
