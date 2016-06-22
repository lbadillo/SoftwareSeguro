package seguro;

import java.awt.EventQueue;


import seguro.visual.GenerateTokenGUI;

public class TransactionNumber {
	
	
	

	public static void main(String[] args) {

		EventQueue.invokeLater(new Runnable() {

			@Override
			public void run() {
				GenerateTokenGUI ex = new GenerateTokenGUI();
				ex.setVisible(true);
			}
		});
	}
}

