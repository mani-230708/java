"""
public class f{
	public static void main(String[] args) {
		int arr[]={1,2,3,4,5};
		boolean sorted=false;
		for(int i=0;i<=3;i++) {
			if(arr[i]<arr[i+1]) {
				//System.out.println(sorted);
				sorted=true;
			}
			else {
				System.out.println("not sorted");
				sorted=false;
				break;

			}
		}
		if(sorted==true) {
			System.out.println("sorted");
		}
	}
}
"""
