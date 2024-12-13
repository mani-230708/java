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
