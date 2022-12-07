package TA7;

class myFile {
    private String path;
    private String password;

    public myFile(String path, String password) {
        this.path = path;
        this.password = password;
    }

}

public class Task1 {

    //    solve the fileLockingProblemDeadlock
    public static void main(String[] args) {
        myFile f = new myFile("path", "pasword");

        Thread t1 = new Thread() {
            public void run() {
                System.out.println(Thread.currentThread().getName()+" trying open the file..");
                synchronized (f) {
                    try {
                        Thread.sleep(3000);
                    } catch (Exception e) {
                    }
                    System.out.println(Thread.currentThread().getName()+" I Have the password and i can open the file !!!");
                }
            }
        };

        Thread t2 = new Thread() {
            public void run() {
                System.out.println(Thread.currentThread().getName()+" trying open the file..");
                synchronized (f) {
                    try {
                        Thread.sleep(3000);
                    } catch (Exception e) {
                    }
                    System.out.println(Thread.currentThread().getName()+ " I Have the password and i can open the file !!!");
                }
            }
        };
        t1.setName("t1");
        t2.setName("t2");
        t1.start();
        t2.start();
    }
}
