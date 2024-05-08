import java.util.Scanner;

class P9317{
	public static void main(String[] args){
		Scanner scn=new Scanner(System.in);

		int t=scn.nextInt();

		for(int tc=1;tc<t+1;tc++){
			int n=scn.nextInt();
			char[] s1=scn.next().toCharArray();
			char[] s2=scn.next().toCharArray();

			int count=0;
			for(int i=0;i<n;i++){
				if(s1[i]==s2[i]){
					count++;
				}
			}

			System.out.println("#"+tc+" "+count);
		}
		return;
	}
}
