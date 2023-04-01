package andyStuff;
//I'm declaring that this program is part of the andyStuff
//package.
//It needs to be in a subdirectory of the project 
//called 'andyStuff.'

//To run this class, go to the parent directory, and
//invoke 'java andyStuff.MyClass'

public class MyClass{
    public static void main(String[] args){
	new MyClass();
    } // end main

    public MyClass(){
	System.out.println("I'm here!");
    } // end constructor
} // end myClass
