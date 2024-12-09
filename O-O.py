principle of object orientation
"""
class fruit{
string name="apple";
int cost=40;
string quality="good";
string color="red";
void eat(){
System.out.println("fruit is eatable");
}
void purchase(){
System.out.println("fruit is purchased");
}
void sweet(){
System.out.println("fruit is sweet");
}
}
"""
class vegetable{
string name;
int cost;
string quality;
int size;
void color(){
System.out.println("vegetable is green color");
}
void sell(){
System.out.println("vegetable is sold");
}
void cook(){
System.out.println("vegetable can be cooked");
}
}
"""
class test{
public static void main(string[] args){
fruit f=new fruit();
vegetable v=new vegetable();
f.eat();
f.purchase();
f.sweet();
v.color();
v.sell();
v.cook();
}
}
"""
