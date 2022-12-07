package TA7;
import java.util.Random;
class Send_Demo
{
    public static void main(String args[])
    {
        Sender send = new Sender();
        ThreadedSend S1 =
                new ThreadedSend( " Hi " , send );
        ThreadedSend S2 =
                new ThreadedSend( " Bye " , send );
        String[]arr= {"Hello ","World ", "I ", "am ", "Ohad "};
        for (int i=0; i<5; i++){
            ThreadedSend t= new ThreadedSend(arr[i], send );
            t.start();
        }

        // Start two threads of ThreadedSend type
        S1.start();
        S2.start();

        // wait for threads to end
        try
        {
            S1.join();
            S2.join();
        }
        catch(Exception e)
        {
            System.out.println("Interrupted");
        }
    }
}
