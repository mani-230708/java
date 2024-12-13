"""
public class Car {
	private String Name;
	private String Color;
	private int Cost;
	private int topspeed;
	private String Country;
	Car(String a,String b,int c,int d,String e){
		super();
		Name=a;
		Color=b;
		Cost=c;
		topspeed=d;
		Country=e;
	}
	public String getName() {
		return Name;
	}
	public String getColor() {
		return Color;
	}
	public int getCost() {
		return Cost;
	}
	public int gettopspeed() {
		return topspeed;
	}
	public String getCountry() {
		return Country;
	}
}
public class Begin {

	public static void main(String[] args) {
		Car c=new Car("civic","red",500000,120,"japan");
		System.out.println(c.getName());
		System.out.println(c.getColor());
		System.out.println(c.getCost());
		System.out.println(c.gettopspeed());
		System.out.println(c.getCountry());
	}
}

"""
