package seguro.visual;

import javax.swing.AbstractAction;
import javax.swing.BorderFactory;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JTextField;
import javax.swing.border.EmptyBorder;


import seguro.logic.CalculateToken;

import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Dimension;
import java.awt.GridLayout;
import java.awt.event.ActionEvent;

public class GenerateTokenGUI extends JFrame {
	private static final long serialVersionUID = -8729770258375329327L;
	private JTextField pin = new JTextField();
	private JTextField account = new JTextField();
	private JTextField amount = new JTextField();
	private JTextField token = new JTextField();
	private JLabel message = new JLabel(); 
	

	public GenerateTokenGUI() {
		initUI();
	}

	private void initUI() {
	    JPanel panel = new JPanel();
	    JPanel panelLa = new JPanel();
	    JPanel panelTe = new JPanel();
		JPanel panel2 = new JPanel();
		
		pin.setDocument(new JTextFieldLimit(9));
		amount.setDocument(new JTextFieldLimit(9));
		
		pin.setToolTipText("Pin Privado (Ejemplo:234567)");
		account.setToolTipText("Cuenta de Correo del Destinatario (Ejemplo: lbd@gmauil.com)");
		amount.setToolTipText("Valor Transaccion (Ejemplo: 50000)");
		
		token.setEditable(false);
		token.setBackground(Color.LIGHT_GRAY);
		
		message.setForeground(Color.RED);
		
		JButton selectb = new JButton("Enviar");
        selectb.setBorder(new EmptyBorder(3, 3, 3, 3));
        selectb.addActionListener(new ClickAction());
        
		setTitle("Generador de Tokens");
		setSize(400, 170);
		setMinimumSize(new Dimension(400, 170));
		setMaximumSize(new Dimension(400, 170));
		setLocationRelativeTo(null);
		setDefaultCloseOperation(EXIT_ON_CLOSE);
		this.setResizable(false);
		

		panel.setBorder(BorderFactory.createEmptyBorder(5, 5, 5, 5));
		panel.setLayout(new BorderLayout(5,5));
		
		panelLa.setLayout(new GridLayout(4, 1, 5, 5));
		panelTe.setLayout(new GridLayout(4, 1, 5, 5));
		panel.add(panelLa, BorderLayout.WEST);
		panel.add(panelTe, BorderLayout.CENTER);
		
		
		panelLa.add(new JLabel("PIN"));
		panelTe.add(pin);
		
		panelLa.add(new JLabel("Destino"));
		panelTe.add(account);
		
		panelLa.add(new JLabel("Valor"));
		panelTe.add(amount);
		
		panelLa.add(new JLabel("Token"));
		panelTe.add(token);
		
		panel2.add(selectb);
		
		
		add(message, BorderLayout.NORTH);
		add(panel,BorderLayout.CENTER);
		add(panel2,BorderLayout.SOUTH );

	}

	private class ClickAction extends AbstractAction {
		/**
		 * 
		 */
		private static final long serialVersionUID = 1L;

		@Override
		public void actionPerformed(ActionEvent e) {
			CalculateToken c = new CalculateToken();
			try{
				if(account.getText().length()<3 ){
					message.setText("Los valores ingresados no son validos");
				}
				else{
					c.setPin(Integer.parseInt(pin.getText()));
					c.setDestination(account.getText());
					c.setAmount(Integer.parseInt(amount.getText()));
					token.setText( c.calculate());
					message.setText(null);
				}
				
			}
			catch (Exception ex){
				message.setText("Los valores ingresados no son validos");
				
			}
			
		}

	}

}
