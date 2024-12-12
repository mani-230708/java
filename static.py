"""
public class test {
	static int a,b,c;
	int m,n,o;
	static {
		a=100;
		b=200;
		c=300;
	}
	{
		a=1001;
		b=2001;
		c=3001;
		m=10001;
		n=20001;
		o=30001;
	}
	static void display() {
		System.out.println(a);
		System.out.println(b);
		System.out.println(c);
	}
	void display1() {
		System.out.println(a);
		System.out.println(b);
		System.out.println(c);
		System.out.println(m);
		System.out.println(n);
		System.out.println(o);
	}

}
public class main {

	public static void main(String[] args) {
		System.out.println(test.a);
		System.out.println(test.b);
		System.out.println(test.c);
		System.out.println("______");
		test t=new test();
		t.display1();
		System.out.println("______");
		test.display();

	}

}
"""
