
public class PackageFunction{		
	public static double sum(int number){
		
		int basePay = 5000;
		double amount = 0;
			if(number < 50){
				amount = number * 160 + basePay;  
			
			}
			if(number >= 50 || amount == 59){
				amount = number * 200 + basePay; 
			
			}
			
			if(number == 60 || amount == 69){
				amount = number * 250 + basePay;
				
			}
			
			if(number > 70){
				amount = number * 500 + basePay;
				
			}
		return amount;
			
		}

	

	

}