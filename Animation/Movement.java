import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

public class Movement extends JFrame implements ActionListener{
  ImageIcon ball;
  Timer clock;
  int x;
  
  public static void main(String args[]){
	  new Movement();
  } // end main
  
  public Movement(){
	  super("Move the ball");
	  //load up the image
	  ball = new ImageIcon("ball.gif");
	  clock = new Timer(50, this);

	  this.setSize(400, 400);
	  this.setVisible(true);
	  this.setDefaultCloseOperation(this.EXIT_ON_CLOSE);
	  
	  
	  clock.start();
  } // end constructor
  
  public void paint(Graphics g) {
	  super.paint(g);
	  g.drawImage(ball.getImage(), x, 100, null);
  } // end paint
  
  public void actionPerformed(ActionEvent e){
	  //happens once each 50 ms
	  x += 5;
	  if (x > 400){
	    x = 0;
	  } // end if
	  
      repaint();
  } // end actionPerformed
  
} // end class def
