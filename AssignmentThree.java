import java.util.Arrays;	
	public class AssignmentThree{
	public static void main(String[] args){
			int[] number = {9,6,9,3,8};
		System.out.print(Arrays.toString(evenOdd(number)));
	}
	public static int[] evenOdd(int[] number){
			int counter = 0;
		for(; counter < number.length; counter++){
			if(number[counter] % 2 == 0){
				number[counter] = 0;
				
			}
			else{
				number[counter] =  1;
			
			}
		}
		return number;
	}
}
		

	