"""
public class vegitables {
	private String name;
	private String color;
	private int cost;
	private int size;
	vegitables(String name,String color,int cost,int size)
	{
		this.name=name;
		this.color=color;
		this.cost=cost;
		this.size=size;
	}
	public String getname() {
		return name;
	}
	public String getcolor() {
		return color;
	}
	public int getcost() {
		return cost;
	}
	public int getsize() {
		return size;
	}
}
public class Test {

	public static void main(String[] args) {
		vegitables v=new vegitables("tomato","red",10,5);
		System.out.println(v.getname());
		System.out.println(v.getcolor());
		System.out.println(v.getcost());
		System.out.println(v.getsize());
	}

}
"""
