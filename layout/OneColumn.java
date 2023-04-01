import java.awt.*;
import javax.swing.*;

public class OneColumn extends JFrame{

	/**
	 * @param args
	 */

	Container p = this.getContentPane();

	public static void main(String[] args) {
		new OneColumn();
	} //
	
	public OneColumn(){
		super("Grid One Column");
		this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		
		p.setLayout(new GridLayout(0, 1));
		
		this.addControls();
        this.setVisible(true);
        this.pack();
	}
	
	public void addControls(){
		p.add(new JButton("short"));
		p.add(new JButton("-- medium --"));
		p.add(new JButton("----- long -----"));
		p.add(new JButton(""));
		p.add(new JButton("-------- really long --------"));
	}

}
