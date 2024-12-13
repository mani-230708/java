"""
class Dog {
	 private String Name;
	 private String Color;
	 private int Cost;
	 private int Age;
	 private String breed;
	 public void setName(String Name) {
		 this.Name=Name;
	 }
	 public String getName() {
		 return Name;
	 }
	 public void setColor(String Color) {
		 this.Color=Color;
	 }
	 public String getColor() {
		 return Color;		 
	 }
	 public void setCost(int Cost) {
		 this.Cost=Cost;
	 }
	 public int getCost() {
		 return Cost;		 
	 }
	 public void Age(int Age) {
		 this.Age=Age;
		 
	 }
	 public int getAge() {
		 return Age;
		 
	 }
	 public void setbreed(String breed) {
		 this.breed=breed;
	 }
	 public String getbreed() {
		 return breed;
	 }
	
}
package m;

public class start {

	public static void main(String[] args) {
		Dog d=new Dog();
		d.setName("tommy");
		d.setColor("black");
		d.setCost(10000);
		d.Age(12);
		d.setbreed("shitzu");
		System.out.println("Name:"+d.getName());
		System.out.println("Color:"+d.getColor());
		System.out.println("Age:"+d.getAge());
		System.out.println("Cost:"+d.getCost());
		System.out.println("breed:"+d.getbreed());
	}
}
"""
