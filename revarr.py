"""
import java.util.*;

 class e {

	public static void main(String[] args) {
		int arr[]=new int[] {4,9,1,6,8};
		int start = 0;
		int end = arr.length-1;
		while(start<end) {
			int temp = arr[start];
			arr[start]=arr[end];
			arr[end]=temp;
			start++;
			end--;
		}
		int i;
		for(i = 0;i<arr.length;i++) {
			System.out.print(" "+(arr[i]));
		}
		
	}

}
"""
