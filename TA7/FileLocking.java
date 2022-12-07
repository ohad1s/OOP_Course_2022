package TA7;

public class FileLocking {

    public static void main(String[] args) {
        final String path = "MyFile.Shit";
        final String password = "123456789";
        // t1 tries to lock resource1 then resource2
        Thread t1 = new Thread() {
            public void run() {
                synchronized (password) {
                    System.out.println("Thread 1: I have the password");

                    try {
                        Thread.sleep(100);
                    } catch (Exception e) {
                    }

                    synchronized (path) {
                        System.out.println("Thread 1: and now I can open the file");
                    }
                }
            }
        };

        // t2 tries to lock resource2 then resource1
        Thread t2 = new Thread() {
            public void run() {
                synchronized (path) {
                    System.out.println("Thread 2: trying open the file");

                    try {
                        Thread.sleep(100);
                    } catch (Exception e) {
                    }

                    synchronized (password) {
                        System.out.println("Thread 2: I need the password");
                    }
                }
            }
        };


        t1.start();
        t2.start();
    }
}
