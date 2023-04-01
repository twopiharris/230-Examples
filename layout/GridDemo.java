import java.awt.*;
import javax.swing.*;

public class GridDemo extends JFrame{

	/**
	 * @param args
	 */

	Container p = this.getContentPane();

	public static void main(String[] args) {
		new GridDemo();
	} //
	
	public GridDemo(){
		super("Grid Demo");
		this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		
		p.setLayout(new GridLayout(2,3));
		
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
