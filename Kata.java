public class Kata{
	
	public static boolean isEven(int number1){
		boolean numb = false;
			if(number1 % 2 == 0){
				numb = true; 
			}
			else{
				numb = false ;
			}
		return numb;
		}

	public static boolean isOdd(int number2){
		boolean numb = false;
			if(number2 % 3 == 1){
				numb = false; 
			}
			else{
				numb = true;
			}
		return numb;
		}
	
	public static int substract(int number1, int number2){
		int substraction = 0;
			if(number1 < number2){
				substraction = number2 - number1;
			}
			else{
				substraction = number1 - number2;
			}
		return substraction;
		}


	public static double divide(int number1, int number2){
		double division =  number1 / number2;
			if(number2 == 0){
				division = 0;
			}
		return division;
		}

	public static int factorsOf(int number){
		int factor = 0;
		int counter = 1;
		while(counter <= number){
			if(number % (counter) == 0){

				factor = factor + 1;
			}
			counter++;
			}
			return factor;

		}

	//public static int isSquare(int number){
		//int squaring = number * number;
			//if(number == 
			//}
			//return = squaring;
	
	public static boolean isPrimeNumber(int number){
		boolean primeNumb = false;
		int count = 0;
		for(int counter = 1; counter <= number; counter++){
			if(number%counter == 0){
				count++;
			}
		}
			if(count == 2){primeNumb = true;}
			return primeNumb;
	}

	public static long factorialOf(int number){
		int counter = 5;
		long factoring = 0;
		while(number >= 1){
			if(number % 2==0){
				factoring = number;
			}
			counter++;
			}
			return factoring;
		}



}
			
	
	

		

		
		
		
	

	

			
				
				
				
		