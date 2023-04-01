import java.awt.*;
import javax.swing.*;

public class FlowDemo extends JFrame{

	Container p = this.getContentPane();

	public static void main(String[] args) {
		new FlowDemo();
	} //
	
	public FlowDemo(){
		super("Flow Layout");
		this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		
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
