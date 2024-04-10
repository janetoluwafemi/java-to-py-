public class CalculatingMultiples{
public static void main(String[] arg){
int sum = 0;
int multiples = 0;
int number = 10;
for(int count = 1; count <= 20000; count++){

		multiples = number * count;
		sum +=  multiples;
	}

System.out.println(sum);



}

}