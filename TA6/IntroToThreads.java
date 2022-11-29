package TA6;

import java.util.Random;
import java.util.concurrent.TimeUnit;

public class IntroToThreads {

    public static void PlayMusic(String music) {
        System.out.println("playing " + music + "..");
    }

    public static void PlayFIFA(String player) {
        System.out.println(player + " scored!");
    }

    public static void main(String[] args) throws InterruptedException {
        MyThread t = new MyThread();
        Thread t2 = new Thread(new MyThread2());
        Thread t3 = new Thread(new Runnable() {
            @Override
            public void run() {
                Random rnd = new Random();
                for (int i = 0; i < 10; i++) {
                    char c = (char) ('a' + rnd.nextInt(26));
                    System.out.println(c);
                    try {
                        TimeUnit.SECONDS.sleep(1);
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                }
            }
        });
        Runnable r = () -> {
            for (int i = 0; i < 20; i++) {
                System.out.println("Ciii");
                try {
                    TimeUnit.MILLISECONDS.sleep(400);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        };
        Thread t4 = new Thread(r);
        t4.start();
        t.start();
        t2.start();
        t3.start();
        PlayMusic("Erev Tov- Lior Narkis");
        TimeUnit.SECONDS.sleep(2);
        PlayFIFA("Cristiano Ronaldo");
    }
}
