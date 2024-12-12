"""
class sample{

	static int add(int a,int b) {
		return a+b;
	}
	static int add(int a,int b,int c) {
		return a+b+c;
	}
	float add(int a,float b) {
		return a+b;
	}
	float add(float a,int b) {
		return a+b;
	}
	static float add(float a,float b) {
		return a+b;
	}
	static double add(int a,float b,double c) {
		return a+b+c;
	}
	double add(float a,int b,double c) {
		return a+b+c;
	}
	double add(float a,double b,int c) {
		return a+b+c;
	}
 }
public class mol{
    
	public static void main(String[] args) {
    	int a=10,b=20,c=30;
		float a1=10.11f,b1=20.22f,c1=30.33f;
		double a2=100.11,b2=200.22,c2=300.33;
		sample s =new sample();
		System.out.println(s.add(a,b));
        System.out.println(s.add(a1,b1));
        System.out.println(s.add(a,b1,c2));
        }
	}
""""
public class o {
	static int add(int a,int b){
		return a+b;
		}
	static int add(int a,int b,int c) {
		return a+b+c;
		}
	public static void main(String[] args) {
		System.out.println("enter 2 parameters:");
		System.out.println(add(4,6));
		System.out.println("enter 3 parameters:");
		System.out.println(add(4,6,7));
	}

}
"""
 
