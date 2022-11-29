package TA6;

import java.util.ArrayList;
import java.util.function.Consumer;

public class lambda {
    public static void main(String[]args){
        ArrayList<Integer> numbers = new ArrayList<Integer>();
        numbers.add(5);
        numbers.add(9);
        numbers.add(8);
        numbers.add(1);
        System.out.println("------ one way --------");
        numbers.forEach( (n) -> { System.out.println(n); } );
        System.out.println("------ second way --------");
//         Java's Consumer interface represents a function which takes in one argument and produces a result.
        Consumer<Integer> method = (n) -> { System.out.println(n*10); };
        numbers.forEach( method );
    }
}
