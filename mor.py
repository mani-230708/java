"""
class bank{
	int getRateofIterest(){
		return 0;
		}
}
class SBI extends bank{
	int getRateofIterest(){
		return 9;
		}
}class AXIS extends bank{
	int getRateofIterest(){
		return 8;
		}
}
class HDFC extends bank{
	int getRateofIterest(){
		return 7;
		}
}
public class mor {

	public static void main(String[] args) {
		SBI b1=new SBI();
		AXIS b2=new AXIS(); 
		HDFC b3=new HDFC();
		System.out.println("the rate of interest of SBI:"+b1.getRateofIterest());
		System.out.println("the rate of interest of AXIS:"+b2.getRateofIterest());
		System.out.println("the rate of interest of HDFC:"+b3.getRateofIterest());
	}
}
"""
class animal {
    void sound() {
        System.out.println("animal makes a sound");
    }
}

class Dog extends animal {
	 @Override
    void sound() {
        System.out.println("Dog barks");
    }
}

public class Main {
    public static void main(String[] args) {
        animal myDog = new Dog();
        myDog.sound(); 
    }
}
"""
