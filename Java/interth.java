public class interth {
    public static void main(String[] arg) {
        final bank b = new bank();
        new Thread() {
            public void run() {
                b.withdraw(1100);
            }
        }.start();

        new Thread() {
            public void run() {
                b.deposit(2000);
            }
        }.start();
    }

}

class bank {
    int bal = 1000;

    synchronized void deposit(int a) {
        System.out.println("Going to deposit");
        bal += a;
        System.out.println("deposit success");
        System.out.println(bal);
        notify();
    }

    synchronized void withdraw(int a) {
        System.out.println("Going to withdraw");
        if (bal < a) { // if (!(bal > a)) {
            try {
                System.out.println("waiting to deposit");
                wait();
            } catch (Exception e) {
            }
        }
        bal -= a;
        System.out.println("withdraw success");
        System.out.println(bal);
    }
}
