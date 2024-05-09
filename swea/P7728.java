import java.util.Scanner;
import java.util.HashSet;

public class P7728{
	public static void main(String[] args){
		Scanner scn=new Scanner(System.in);
		int t=scn.nextInt();

		for(int tc=1;tc<t+1;tc++){
			HashSet<Character> cs=new HashSet<>();
			String s=scn.next();
			for(char c:s.toCharArray()){
				cs.add(c);
			}
			System.out.println("#"+tc+" "+cs.size());
		}
		return;
	}
}
