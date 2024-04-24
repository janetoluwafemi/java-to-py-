import java.util.Arrays;
	public class AssignmentTwo{
		public static void main(String[] args){
			int[] number = {2,3,4,5};
		System.out.print(Arrays.toString(doubleNum(number)));
	}

	public static int[] doubleNum(int[] number){
			int count = 0;
			int counter = 0;
		for(; counter < number.length; counter++){
		}
			//System.out.print(Arrays.toString(number));
	
			for(; count < counter; count++){
				number[count] = number[count] * number[count];
			}
		
		//System.out.print(Arrays.toString(number));
		return number;
	}
}			