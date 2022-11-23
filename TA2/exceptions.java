package TA2;

public class exceptions {

    public static void ex1(){
        int data= 10/0;
        System.out.println("rest of code..");
    }

    public static void handle_ex1(){
        int data;
        try{
            data= 10/0;
        }
        catch (ArithmeticException err){
            System.out.println(err);
            err.printStackTrace();
        }
        System.out.println("rest of code..");
    }

    public static void ex2(){
        int data;
        try{
            data= 25/5;
            System.out.println(data);
        }
        catch (Exception err){
            System.out.println(err);
            err.printStackTrace();
        }
        finally {
            System.out.println("finally code..");
        }
        System.out.println("rest of code..");
    }


    public static void handle_ex2(){
        int data;
        try{
            data= 25/0;
            System.out.println(data);
        }
        catch (ArithmeticException err){
            System.out.println("Catch you!");
            System.out.println(err);
            err.printStackTrace();

        }
        finally {
            System.out.println("finally code..");
        }
        System.out.println("rest of code..");
    }

    public static boolean buy_beer(int amount,  int age) throws Exception{
        if (age<18){
            throw new Exception("Age must be over 18");
        }
        else{
            System.out.println(amount+" beers for me please");
            return true;
        }
    }

    public static boolean buy_beer2(int amount,  int age) throws Exception{
        if (age<18){
            throw new InvalidAgeException("Age must be over 18");
        }
        else{
            System.out.println(amount+" beers for me please");
            return true;
        }
    }


    public static void main(String[]args) throws Exception {
//        ex1();
//
//        handle_ex1();
//
//        ex2();
//
//        handle_ex2();
//
        boolean beer;
        try{
            beer= buy_beer2(25,17);
        }
        catch (InvalidAgeException err){
            System.out.println("Cant buy a beer");
            beer= false;
        }
        finally {
            System.out.println("Ciii");
        }

    }
}
