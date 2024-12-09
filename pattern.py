1
"""
class Main{
public static void main(String[] args){
for(int i=0;i<5;i++)
{
System.out.print("#");
}
System.out.println();
"""
2
"""
class Main{
public static void main(String[] args){
for(int i=0;i<5;i++)
{
for(int j=0;j<5;j++)
{
System.out.print("*");
}
System.out.println();
}
}
}
"""
3
"""
class Main{
public static void main(String[] args){
for(int i=0;i<5;i++)
{
for(int j=0;j<=i;j++)
{
System.out.print("*");
}
System.out.println();
}
}
}
"""
4
"""
class Main{
public static void main(String[] args){
for(int i=0;i<5;i++)
{
for(int j=i;j<5;j++)
{
System.out.print("*");
}
System.out.println();
}
}
}
"""
5
"""
class Main{
public static void main(String[] args){
for(int i=0;i<5;i++)
{
for(int j=0;j<5;j++)
{
System.out.print(i);/System.out.print(j);
}
System.out.println();
}
}
}
"""
6
"""
class Main{
public static void main(String[] args){
int n=1;
for(int i=0;i<5;i++)
{
for(int j=0;j<=i;j++)
{
System.out.print(n);
n++;
}
System.out.println();
}
}
}
"""
7
"""
class Main{
public static void main(String[] args){
for(int i=0;i<5;i++)
{
for(int j=0;j<5;j++)
{
System.out.print(-);
}
for(int j=0;j<5;j++)
{
System.out.print(#);
}
System.out.println();
}
}
}
"""
8
"""
class Main{
public static void main(String[] args){
for(int i=0;i<5;i++)
{
for(int j=i;j<5;j++)
{
System.out.print(-);
}
for(int j=0;j<=i;j++)
{
System.out.print(*);
}
System.out.println();
}
}
}
"""
9
"""
class Main{
public static void main(String[] args){
for(int i=0;i<5;i++)
{
for(int j=0;j<=(2*i-1);j++)
{
System.out.print(-);
}
System.out.println();
}
}
}
"""
10
"""
class Main{
public static void main(String[] args){
int n=5;
for(int i=1;i<n;i++)
{
for(int j=1;j<n;j++)
{
if(i==1||i==n||j==1||j==n)
{
System.out.print("* ");
}
else
{
System.out.println(" ");
}
}
System.out.print();
}
}
}
