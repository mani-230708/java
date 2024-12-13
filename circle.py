""""
import java.util.Scanner;
public class pi {
	static double pi;
	double radius;
	double area;
	static {
		pi=3.14;
	}
	void collectdata() {
		Scanner sc=new Scanner(System.in);
		System.out.println("enter the radius:" );
		radius=sc.nextDouble();
	}
	void calculate() {
		area=pi*radius*radius;
	}
	void display() {
		System.out.println("area is:"+area);
	}

}
public class circle {

	public static void main(String[] args) {
		pi c=new pi();
		c.collectdata();
		c.calculate();
		c.display();
	}

}
"""
