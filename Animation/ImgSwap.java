import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

public class ImgSwap extends JFrame implements ActionListener{
  ImageIcon[] ball = new ImageIcon[6];
  Timer clock;
  int frame;
  
  public static void main(String args[]){
	  new ImgSwap();
  } // end main
  
  public ImgSwap(){
	  super("Animate Images");
	  //load up the images
	  ball[1] = new ImageIcon("jball1.gif");
	  ball[2] = new ImageIcon("jball2.gif");
	  ball[3] = new ImageIcon("jball3.gif");
	  ball[4] = new ImageIcon("jball4.gif");
	  ball[5] = new ImageIcon("jball5.gif");
	  clock = new Timer(100, this);

	  this.setSize(400, 400);
	  this.setVisible(true);
	  this.setDefaultCloseOperation(this.EXIT_ON_CLOSE);
	  
	  
	  clock.start();
  } // end constructor
  
  public void paint(Graphics g) {
	  super.paint(g);
	  g.drawImage(ball[frame].getImage(), 150, 150, null);
  } // end paint
  
  public void actionPerformed(ActionEvent e){
	  //happens once each 50 ms
	  frame++;
	  if (frame > 5){
	    frame = 1;
	  } // end if
	  
      repaint();
  } // end actionPerformed
  
} // end class def


