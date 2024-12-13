constructor chaining
"""
public class Parent {
	Parent(){
		super();
		System.out.println("inside the Parent constructor");		
	}
}
class Child extends Parent{
	Child(){
		System.out.println("inside the Child constructor");
	}
}
public class SampleCode {

	public static void main(String[] args) {
		Child c11=new Child();
	}

}
"""
local chaining
"""
public class Human {
	private String Name;
	private String Location;
	private int Age;
	private double Height;
	private double Weight;
	Human(String a,String b,int c,double d,double e){
		this( "ramu","banglore",21,176.9);
		Name=a;
		Location=b;
		Age=c;
		Height=d;
		Weight=e;
	}
	Human(String a,String b,int c,double d){
		this( "shamu","hyderabad",20);
		Name=a;
		Location=b;
		Age=c;
		Height=d;
	}
	Human(String a,String b,int c){
		Name=a;
		Location=b;
		Age=c;
	}
	
	public String getName() {
		return Name;
	}
	public String getLocation() {
		return Location;
	}
	public int getAge() {
		return Age;
		
	}
	public double getHeight() {
		return Height;
	}
	public double getWeight() {
		return Weight;
	}
	
}
public class LaunchAgain {

	public static void main(String[] args) {
		Human h=new Human("sunny","chennai",19,156.7,65);
		System.out.println(h.getName());
		System.out.println(h.getLocation());
		System.out.println(h.getAge());
		System.out.println(h.getHeight());
		System.out.println(h.getWeight());

	}

}
"""
