import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

public class KeyInput extends JFrame implements KeyListener{
  ImageIcon ball;
  int x;
  
  public static void main(String args[]){
	  new KeyInput();
  } // end main
  
  public KeyInput(){
	  super("KeyboardInput");
	  //load up the image
	  ball = new ImageIcon("ball.gif");

	  this.setSize(400, 400);
	  this.setVisible(true);
	  this.setDefaultCloseOperation(this.EXIT_ON_CLOSE);

	  //specify I am my own keyboard listener
          this.addKeyListener(this);	  
	  
  } // end constructor
  
  public void paint(Graphics g) {
	  super.paint(g);
	  g.drawImage(ball.getImage(), x, 100, null);
  } // end paint
  
  //the following methods are required for a keyListener

  public void keyTyped(KeyEvent e){
	//responds after press and release cycle
    } // end keyTyped

  public void keyPressed(KeyEvent e){
        //use for continuous keyboard input
        int theKey = e.getKeyCode();
        System.out.println(theKey);
	if (theKey == KeyEvent.VK_LEFT){
	    x -= 5;
        } else if (theKey == KeyEvent.VK_RIGHT){
            x += 5;
        } // end if
        repaint();
  } // end keyPressed

  public void keyReleased(KeyEvent e){
	//occurs when key is released
    } // end keyReleased

} // end class def
