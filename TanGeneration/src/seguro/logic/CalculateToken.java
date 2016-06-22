package seguro.logic;


import java.util.Random;

public class CalculateToken {
	
	private int pin;
	private String  destination;
	private int amount;
	private int token;
	private int FACTOR = 61;
	
	
	public int getPin() {
		return pin;
	}

	public void setPin(int pin) {
		this.pin = pin;
	}

	public String getDestination() {
		return destination;
	}

	public void setDestination(String destination) {
		this.destination = destination;
	}

	public int getAmount() {
		return amount;
	}

	public void setAmount(int amount) {
		this.amount = amount;
	}

	public int getToken() {
		return token;
	}

	public void setToken(int token) {
		this.token = token;
	}
	
	public String calculatePin (String correo){
		String res=null;
		long topin=0L;
		long i=1L;
		long size = (long)correo.toCharArray().length;
		for (char v : correo.toCharArray()){
			topin=(i*(long)v)+topin+size;
			i++;
		}
		topin=topin*topin;
		topin=topin % 999999999L; 
		res=String.valueOf((long)topin);
		return res;
		
	}
	
	public int calculateRandom(){
		Random randomGenerator = new Random();
		return randomGenerator.nextInt(100);
	}

	
	public String calculate(){
		int random=calculateRandom();
		long pin2 = Long.parseLong(calculatePin(destination));
		long total=pin + pin2 + ((long)amount*((long)random + (long)FACTOR));
		
		return total+"-"+random;
	}
	
	

}
