space count
"""
public class i {

	public static void main(String[] args) {
		int count=0;
		String words="Hello good morning";
		for(int i=0;i<words.length();i++)
		{
			if(words.charAt(i)==' ')
			{
				count++;
			}
		}
		System.out.println(count+1);
	}

}
"""
vowal count
"""
public class j {

	public static void main(String[] args) {
		int vowelcount=0;
		String words="Hello good morning";
		for(int i=0;i<words.length();i++)
		{
			char ch=words.charAt(i);

			if(ch=='a'||ch=='e'||ch=='i'||ch=='o'||ch=='u') 
			{
				vowelcount++;
			}
		}
		System.out.println(vowelcount);
	}

}
"""
words count
"""
public class j {
   public static void main(String[] args) {
   String words="Hello good morning";
   System.out.println(words.length());
   }
}
"""
public class k {
	public static void main(String[] args) {
		 String str1=new String("hello");
		 str1.concat("good");
		 String str2=str1.concat("morning");
		 str1=str1.concat("hi");
		 System.out.println(str1);
		 System.out.println(str2);
	}

}
"""
reverse 1
"""
package mani;

public class l {

	public static void main(String[] args) {
		String words="hello good morning";
        for(int i=words.length()-1;i>=0;i--)
        {
        	System.out.print(words.charAt(i));
        }
    }
}
"""
reverse 2
"""
public class m {

    public static void main(String[] args) {
    	String words="hello good morning";
		String output="";
		String[] s=words.split(" ");
		for(int i=0;i<s.length;i++) {
			for(int j=s[i].length()-1;j>=0;j--) {
				output+=s[i].charAt(j);
			}
			output=output+" ";
		}
		System.out.print(output);

	}

}
"""


   

