import java.awt.*;
import java.applet.*;
import java.awt.event.*;
import ShowImage;

public class AnimDemo extends Applet implements ActionListener {

    Button btnShowImage = new Button("ShowImage");

    public void init(){
	this.setLayout(new FlowLayout());
        this.add(btnShowImage);
        
        btnShowImage.setActionListener(this);
    } // end init

    public void actionPerformed(ActionEvent e){
        System.out.println("I got clicked");
    } // end actionPerformed;
} // end AnimDemo

