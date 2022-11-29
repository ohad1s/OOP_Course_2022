package TA6;

import java.util.concurrent.TimeUnit;

public class MyThread extends Thread {
    public void run() {
        for (int i=0; i<10; i++){
            System.out.println(i);
            try {
                TimeUnit.SECONDS.sleep(1);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}
