import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

public class Bouncing extends JFrame implements ActionListener{
  ImageIcon ball;
  Timer clock;
  int x, y;
  int dx, dy;
  
  public static void main(String args[]){
	  new Bouncing();
  } // end main
  
  public Bouncing(){
	  super("Bouncing Ball");
	  //load up the image
	  ball = new ImageIcon("ball.gif");
	  clock = new Timer(50, this);
	  dx = 5;
	  dy = 3;
	  
	  this.setSize(400, 400);
	  this.setVisible(true);
	  this.setDefaultCloseOperation(this.EXIT_ON_CLOSE);
	  
	  clock.start();
  } // end constructor
  
  public void paint(Graphics g) {
	  super.paint(g);
	  
	  g.drawImage(ball.getImage(), x, y, null);
  } // end paint
  
  public void actionPerformed(ActionEvent e){
	  //happens once each 50 ms
	  x += dx;
	  y += dy;
	  
	  checkBounds();
	  
      repaint();
  } // end actionPerformed
  
  public void checkBounds(){
	  if (x > this.getWidth() - ball.getIconWidth()){
		  dx *= -1;
	  } // end if
	  if (x < 0){
		  dx *= -1;
	  } // end if
	  if (y > this.getHeight()- ball.getIconHeight()){
		  dy *= -1;
	  } // end if
	  if (y < 0){
		  dy *= -1;
	  } // end if
  } // end checkBounds
  
} // end class def
