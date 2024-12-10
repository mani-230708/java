1d
"""
import java.util.Scanner;

public class b {

	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		String arr[]=new String[5];
		for(int i=0;i<5;i++)
		{
			System.out.println("enter the name of employee no:"+(i+1));
			arr[i]=sc.next();
		}
		for(String name:arr)
		{
			System.out.println(name);
		}
		

	}

}
"""
2d
"""
import java.util.Scanner;

public class c {

	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		String arr[][]=new String[2][5];
		for(int i=0;i<2;i++)
		{
			for(int j=0;j<5;j++) {
			System.out.println("enter employee name:"+(j+1));
			arr[i][j]=sc.next();
		}
		}
		for(int i=0;i<2;i++)
		{
			System.out.println("company no:"+(i+1));
			for(int j=0;j<5;j++)
			{
				System.out.println(arr[i][j]);
			}
		}
	}
}
"""
3d
"""
