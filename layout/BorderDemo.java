import java.awt.*;
import javax.swing.*;

public class BorderDemo extends JFrame{

	/**
	 * @param args
	 */

	Container p = this.getContentPane();

	public static void main(String[] args) {
		new BorderDemo();
	} //
	
	public BorderDemo(){
		super("Border Demo");
		this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		
		p.setLayout(new BorderLayout());
		
		this.addControls();
        this.setVisible(true);
        this.pack();
	}
	
	public void addControls(){
		//note I now must include an area
		p.add(new JButton("short"), BorderLayout.EAST);
		p.add(new JButton("-- medium --"), BorderLayout.NORTH);
		p.add(new JButton("----- long -----"), BorderLayout.SOUTH);
		p.add(new JButton(""), BorderLayout.WEST);
		p.add(new JButton("-------- really long --------"), BorderLayout.CENTER);
	}

}
