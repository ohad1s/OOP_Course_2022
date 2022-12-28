package TA10_java;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;

public class SumRange {
    private static final int NUM_THREADS = 4;  // Number of threads to use

    public static long sumRange(int n) {
        if (n < 1) {
            return 0;
        }

        long sum = 0;
        int chunkSize = n / NUM_THREADS;  // Size of each chunk

        // Create a thread pool and submit tasks to sum each chunk
        ExecutorService executor = Executors.newFixedThreadPool(NUM_THREADS);
        for (int i = 1; i <= NUM_THREADS; i++) {
            int start = (i - 1) * chunkSize + 1;
            int end = i * chunkSize;
            if (i == NUM_THREADS) {
                end = n;  // Last chunk may be larger
            }
            executor.submit(new SumTask(start, end));

        }
        executor.shutdown();
//        The shutdown method is called to terminate the thread pool once all
//        tasks have been submitted, and the awaitTermination method is used to wait
//        for all tasks to complete before proceeding. - same like join for each thread

        // Wait for all tasks to complete and sum the results
        try {
            executor.awaitTermination(1, TimeUnit.DAYS);
            for (long partialSum : SumTask.getPartialSums()) {
                sum += partialSum;
            }
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        return sum;
    }

    public static void main(String[]args){
        long sum= sumRange(1000000);
        System.out.println(sum);
    }
}


