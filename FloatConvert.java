import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.*;

/**
 * 
 */

/**
 * @author aharris
 * practice converting float point binary to dec with ABBBBCDD format
 * A = sign mantissa
 * B = mantissa
 * C = sign exponent
 * D = exponent
 */
public class FloatConvert extends JApplet implements ActionListener {

   JTextField txtBin = new JTextField();
   JTextField txtDec = new JTextField();
   JButton btnBin = new JButton("random bin");	
   JButton btnDec = new JButton("random dec");	
   JButton btnCheck = new JButton("check answer");
   JButton btnTellMe = new JButton("tell me");
   JLabel response = new JLabel("Click to get random value");
   
   String sm;		//sign of mantissa
   int m;			//mantissa
   String mBin;
   String se;		//sign of exponent
   int e;			//exponent
   String eBin; 
   String binFloat;	//generated number in binary ABBBBCDD format
   double decFloat; //generated number as a double;
   
   //use arrays to rather than built-in conversion
   //to keep leading spaces for formatting.
   String[] bin4 = {"0000", "0001", "0010", "0011",
		            "0100", "0101", "0110", "0111",
   			        "1000", "1001", "1010", "1011",
		   			"1100", "1101", "1110", "1111"
                };
   String[] bin2 = { "00", "01", "10", "11"};

   
	public FloatConvert(){
      Container mainPanel = this.getContentPane();
      mainPanel.setLayout(new BorderLayout());
      
      Panel panel = new Panel();
      
      panel.setLayout(new GridLayout(0,2));
      
      panel.add(new JLabel("binary value"));
      panel.add(txtBin);
      
      panel.add(new JLabel("decimal value"));
      panel.add(txtDec);
      
      panel.add(btnBin);
      panel.add(btnDec);
      
      panel.add(btnCheck);
      panel.add(btnTellMe);
      
      mainPanel.add(panel, BorderLayout.CENTER);
      mainPanel.add(response, BorderLayout.SOUTH);
      
      btnBin.addActionListener(this);
      btnDec.addActionListener(this);
	  btnCheck.addActionListener(this);
	  btnTellMe.addActionListener(this);
	} // end constructor
	
	public void actionPerformed(ActionEvent e) {
      if (e.getSource() == btnBin){
    	  this.getRandom();
    	  txtBin.setText(binFloat);
    	  txtDec.setText("");
      } // end if
      if (e.getSource() == btnDec){
    	  this.getRandom();
    	  txtBin.setText("");
    	  txtDec.setText(String.valueOf(decFloat));
      } // end if
      if (e.getSource() == btnCheck){
    	  this.checkAns();
      } // end if
      if (e.getSource() == btnTellMe){
    	  this.tellMe();
      } // end if
	}
	
	/**
	 * @param args
	 * @return 
	 */

	public void getRandom(){
		// generates random value
		java.util.Random rg = new java.util.Random();
		
		//get sign of Mantissa
		int temp = rg.nextInt(2);
		sm = String.valueOf(temp);
		m = rg.nextInt(15);
		mBin = bin4[m];
		temp = rg.nextInt(2);
		se = String.valueOf(temp);
		e = rg.nextInt(3);
		eBin = bin2[e];
		
		binFloat = sm + mBin + se + eBin;
		decFloat = m;
		if (sm.equals("1")){
			decFloat *= -1;
		}

		temp = e;
		if (se.equals("1")){
		  temp *= -1;
		} // end if
		double exp = Math.pow(2, temp);
		decFloat *= exp;
		
		txtBin.setText(binFloat);
		txtDec.setText(String.valueOf(decFloat));
	} // end getRandom 
	
	public void checkAns(){
		boolean correct = true;
		String output = "";
		if (!txtBin.getText().equals(binFloat)){
			correct = false;
			output = "Problem with binary value";
		} // end if
		if (!txtDec.getText().equals(String.valueOf(decFloat))){
			correct = false;
			output = "Problem with decimal value";
		} // end if
		
		if (correct){
			output = "Great Job!";
		} // end if
		response.setText(output);
		
	} // end checkAns
	
	public void tellMe(){
		//reveal the values
		response.setText("binary: " + binFloat + ", decimal" + String.valueOf(decFloat));
	} // end tellMe
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
        new FloatConvert();
	} // end main

} // end class def
