import java.util.Scanner;
	public class Packages{
	public static void main(String[] args){

	Scanner scanner = new Scanner(System.in);
		System.out.print("Enter a valid number: ");
		int number = scanner.nextInt();

	double sumb = PackageFunction.sum(number);
	System.out.print(sumb);

	}

}




	