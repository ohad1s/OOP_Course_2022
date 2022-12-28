package TA10_java;

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.*;

public class MaximumFinder_ThreadPool_futures {

    public static int findMax(int[] array) {
        int max = Integer.MIN_VALUE;
        for (int i : array) {
            max = Math.max(max, i);
        }
        return max;
    }
}


class MaxFinder2 {

    public static int maxFinderTask(int start, int end, int[]array) {
        int max = Integer.MIN_VALUE;
        for (int i = start; i < end; i++) {
            max = Math.max(max, array[i]);
        }
        return max;
    }

    public static int findMax(int[] array,int num_threads) {
        ArrayList<Future>futures= new ArrayList<>();
        if (array.length == 0) {
            return 0;
        }

        int max = Integer.MIN_VALUE;
        int chunkSize = array.length / num_threads;  // Size of each chunk

        ExecutorService executor = Executors.newFixedThreadPool(num_threads);
        for (int i = 1; i <= num_threads; i++) {
            int start = (i - 1) * chunkSize + 1;
            int end = i * chunkSize;
            if (i == num_threads) {
                end = array.length;  // Last chunk may be larger
            }
            int finalEnd = end;
            Future<Integer>future = (Future<Integer>) executor.submit(()->maxFinderTask(start, finalEnd,array));
            futures.add(future);

        }
        executor.shutdown();

        // Wait for all threads to complete and get the maximum values
        try {
            executor.awaitTermination(1, TimeUnit.DAYS);
            for (Future f : futures) {
                int x= (Integer)f.get();
                if (x>max){
                    max=x;
                }
            }
        } catch (InterruptedException | ExecutionException e) {
            e.printStackTrace();
        }

        return max;
    }
    public static void main(String[]args){
        int[] array= {9,45,6,7,87,32,5,23,54,65,76,3,2,5456,2321,545,56,322,121,657,3,2365,623,5423,325,65,23,546,2,54,21,65,73,46,5,232,665,6,3242,6544,213,645,5345};
        int max = findMax(array,4);
        System.out.println(max);
    }
}

class MaxTask2 implements Runnable {
    private static final List<Integer> partialMaxes = new ArrayList<>();  // List to store partial maxes

    private final int[] array;  // Array to search
    private final int start;    // Start of range
    private final int end;      // End of range

    public MaxTask2(int[] array, int start, int end) {
        this.array = array;
        this.start = start;
        this.end = end;
    }

    @Override
    public void run() {
        int max = Integer.MIN_VALUE;
        for (int i = start; i < end; i++) {
            max = Math.max(max, array[i]);
        }
        partialMaxes.add(max);  // Add partial max to list
    }

    public static List<Integer> getPartialMaxes() {
        return partialMaxes;
    }
}

