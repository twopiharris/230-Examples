import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class Bmi extends JApplet implements ActionListener{
    JTextField txtFeet = new JTextField("6");
    JTextField txtInches = new JTextField("0");
    JTextField txtPounds = new JTextField("180");
    JLabel lblBmi = new JLabel("0");
    JLabel lblStatus = new JLabel("");
	JButton btnCalc = new JButton("calculate");
	
	public void init(){
	  
	  //set up input layer
	  JPanel pnlInput = new JPanel();
	  pnlInput.setLayout(new GridLayout(0,2));
	  
	  //add components
	  pnlInput.add(new JLabel("feet"));
	  pnlInput.add(txtFeet);
	  
	  pnlInput.add(new JLabel("inches"));
	  pnlInput.add(txtInches);
	  
	  pnlInput.add(new JLabel("weight (pounds)"));
	  pnlInput.add(txtPounds);
	  
	  pnlInput.add(new JLabel("Body Mass Index"));
	  pnlInput.add(lblBmi);
	  
	  pnlInput.add(new JLabel("Status"));
	  pnlInput.add(lblStatus);
	  
      //set up button layer
	  JPanel pnlButton = new JPanel();
	  pnlButton.setLayout(new FlowLayout());
	  pnlButton.add(btnCalc);
	  
	  //set up main layout
	  Container pnlMain = this.getContentPane();
	  pnlMain.setLayout(new BorderLayout());
      pnlMain.add(pnlInput, BorderLayout.CENTER);
      pnlMain.add(pnlButton, BorderLayout.SOUTH);
      
      btnCalc.addActionListener(this);
  } // end init

  public void actionPerformed(ActionEvent e){
	  int feet = Integer.valueOf(txtFeet.getText());
	  int inches = Integer.valueOf(txtInches.getText());
	  int weight = Integer.valueOf(txtPounds.getText());
	  
	  int height = (feet * 12) + inches;
	  double bmi = (weight * 703) / (height * height);
      lblBmi.setText(String.valueOf(bmi));
	  String status = "";
	  if (bmi < 18.5){
		  status = "underweight";
	  } else if (bmi <= 24.9){
		  status = "normal";
	  } else if (bmi <= 29.9){
		  status = "overweight";
	  } else {
		  status = "obese";
	  } // end if
      
      lblStatus.setText(status);
  } // end actionPerformed
 
} // end applet

