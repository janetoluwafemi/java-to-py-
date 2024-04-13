import java.util.Scanner;
	public class Calculation{
		public static void main(String[] args){
	
		Scanner scanner = new Scanner(System.in);

		System.out.println("Enter a number: ");
		int number1 = scanner.nextInt();

		System.out.println("Enter a second number: ");
		int number2 = scanner.nextInt();

	boolean num = Kata.isEven(number1);
	System.out.println( num );

	boolean numb = Kata.isEven(number2);
	System.out.println( numb );

	int substracts = Kata.substract(number1, number2);
	System.out.printf("The Substraction is: %d%n" , substracts);

	double divides = Kata.divide(number1, number2);
	System.out.printf("The Division is: %f%n" , divides);

	int factor = Kata.factorsOf(number1);
	System.out.printf("The Factors are: %d%n" , factor);

	boolean prime = Kata.isPrimeNumber(number1);
	System.out.print(prime);

	long factorial = Kata.factorialOf(number1);
	System.out.printf("The Factorial is: %d%n" , factorial);




	

	

}


}