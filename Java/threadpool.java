import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class threadpool {
    public static void main(String[] args) {

        ExecutorService ex = Executors.newFixedThreadPool(5); // 5 threads per pool

        for (int i = 0; i < 10; i++) {
            Runnable r = new WorkerThread("  " + i);
            ex.execute(r);
        }
        ex.shutdown();
        while (!ex.isTerminated()) {   }  
        System.out.println("Finished all threads");
    }
}

class WorkerThread implements Runnable {
    private String m;

    WorkerThread(String s) {
        m = s;
    }

    @Override
    public void run() {
        System.out.println(Thread.currentThread().getName() + "  " + m);
        ts();
        System.out.println(Thread.currentThread().getName() + "End ");

    }

    public void ts() {
        try {
            Thread.sleep(1000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}