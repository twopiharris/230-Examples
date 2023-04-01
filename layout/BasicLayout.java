import java.awt.*;
import javax.swing.*;

public class BasicLayout extends JFrame{

	/**
	 * @param args
	 */

	Container p = this.getContentPane();

	public static void main(String[] args) {
		new BasicLayout();
	} //
	
	public BasicLayout(){
		super("Flow Layout");
		p.setLayout(new FlowLayout());
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
