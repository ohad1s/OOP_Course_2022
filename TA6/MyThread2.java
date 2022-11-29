package TA6;

import java.util.concurrent.TimeUnit;

public class MyThread2 implements Runnable {
    @Override
    public void run() {
        for (int i = 10; i > 0; i--) {
            System.out.println(i * 10);
            try {
                TimeUnit.SECONDS.sleep(1);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}
