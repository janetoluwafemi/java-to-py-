import java.util.Arrays;	
	public class AssignmentFour{
	public static void main(String[] args){
			int[] number = {9,6,9,3,8};
		System.out.print(Arrays.toString(evenOdd(number)));
	}
	public static String[] evenOdd(int[] numb){
			int counter = 0;
			String[] number = new String[5]; 
		int count = 0;
		for(; counter < number.length; counter++){
			if(numb[counter] % 2 == 0){
				number[count] = "false";
				count++;
			}
			else{
				number[count] =  "true";
				count++;
			}
		}
		return number;
	}
}