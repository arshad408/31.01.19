class Abc 
{ 
public static void main (String[] args) 
{ 
	int x = 5, y = 10; 
	x = x ^ y ^ (y = x); 
	System.out.println("After Swapping values of x and y are "
						+ x + " " + y); 
} 
} 
