import java.util.Scanner;
	public class Receipt1{
	public static void main(String[] args){

	Scanner scanner = new Scanner(System.in);
	//System.out.println("How many goods picked up: ");
	//int goodspicked = scanner.nextInt();
	int goodspicked = 1;
	//String name =  scanner.next();
	
	String name = null;
	String nameCus = null;
	System.out.println("Customer's Name");
	nameCus = scanner.next();
	double discountAmount = 0.0;
	double[] total = new double[goodspicked];
	String[] items = new String[goodspicked];
	int[] number = new int[goodspicked];
	int[] amount = new int[goodspicked];
	boolean moreItems = true;	
	double totalSum = 0.0;
	double vat = 0.0;
	double billTotal = 0.0;
	int counter = 0;
	for(; moreItems != false; counter++){

		System.out.println("What did the user buy: ");
		items[counter] = scanner.next();

		System.out.println("How many pieces: ");
		number[counter]  = scanner.nextInt();
	
		System.out.println("How much per unit: ");
		amount[counter] = scanner.nextInt();
	
		System.out.println("Add more items: ");
		moreItems = scanner.nextBoolean();

	}
System.out.println("What is cashier name?: ");
name = scanner.next();
System.out.println("How much discount will he get: ");
int discount = scanner.nextInt();
	
	for(int count = 0; count < counter ; count++){ 
		total[count] = number[count] * amount[count];
		totalSum += total[count]; 
	}
discountAmount = discount * totalSum / 100;

vat = totalSum * 7.50 / 100;
billTotal = (totalSum - discountAmount) + vat;
System.out.println("How much did the customer give to you?: ");
int amountPaid = scanner.nextInt();

double balance = billTotal - amountPaid;

System.out.println("SEMICOLON STORES");
System.out.println("MAIN BRANCH");
System.out.println("Location: 312, HERBERT MACAULAY WAY, SABO YABA, LAGOS.");
System.out.println("Tel: 03293828343");
System.out.println("Date: 18-Dec-22 8:43:11 pm");
System.out.println("Cashier: " + name);
System.out.println("Customer Name: " + nameCus);
System.out.printf("ITEM "  , "QTY "  ,  "PRICE "  ,  "TOTAL(NGN) ");
	int count = 0;
	for(int counti = 0; counti < count; counti++){	
		System.out.printf("number[counter]: %d%n" , number   ,    "amount[counter]: %.2f%n" , amount   ,    "total[counter]: %.2f%n" , total);
	}
	
System.out.printf("totalSum: %.2f%n" , totalSum);
System.out.printf("discount: %d%n" ,  discount);
System.out.printf("vat@: %.2f%n" ,  vat);
System.out.printf("billTotal: %.2f%n" ,  billTotal);
System.out.printf("Amount Paid: %d%n" ,  amountPaid);
System.out.printf("Balance: %.2f%n" ,  balance);


System.out.print("Thank You For Your Patronage");




}


}



	 