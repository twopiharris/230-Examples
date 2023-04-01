import java.awt.*;
import javax.swing.*;

public class PanelDemo extends JFrame{

	Container p = this.getContentPane();

	public static void main(String[] args) {
		new PanelDemo();
	} //
	
	public PanelDemo(){
		super("Panel Demo");
		this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		
		p.setLayout(new BorderLayout());
		
		this.addControls();
        this.setVisible(true);
        this.pack();
	}
	
	public void addControls(){
		//build the center panel
		Panel pCenter = new Panel();
		pCenter.setLayout(new GridLayout(0,1));
		pCenter.add(new JButton(""));
		pCenter.add(new JButton("-------- really long --------"));

		//build the south panel
		Panel pSouth = new Panel();
		pSouth.setLayout(new FlowLayout());
		pSouth.add(new JButton("short"));
		pSouth.add(new JButton("-- medium --"));
		pSouth.add(new JButton("----- long -----"));

        //build the main panel
		p.add(pCenter, BorderLayout.CENTER);
		p.add(pSouth, BorderLayout.SOUTH);
	} // end add controls

}
