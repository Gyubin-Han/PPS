import java.util.Scanner;
import java.util.List;
import java.util.ArrayList;

class P6730{
	public static void main(String[] args){
		Scanner scn=new Scanner(System.in);
		int t=scn.nextInt();
		
		for(int tc=1;tc<t+1;tc++){
			int n=scn.nextInt();
			List<Integer> arr=new ArrayList<>();

			arr.add(scn.nextInt());
			int mx,mi;
			mx=mi=0;
			for(int i=1;i<n;i++){
				arr.add(scn.nextInt());
				int sum=arr.get(i)-arr.get(i-1);

				if(sum>0 && sum>mx){
					mx=sum;
				}else if(sum<0 && sum<mi){
					mi=sum;
				}
			}

			System.out.println("#"+tc+" "+mx+" "+(-mi));
		}
		return;
	}
}