package TA10_java;

import java.util.ArrayList;
import java.util.List;

public class MaximumFinder {

    public static int findMax(int[] array) {
        int max = Integer.MIN_VALUE;
        for (int i : array) {
            max = Math.max(max, i);
        }
        return max;
    }
}


class MaxFinder {

    public static int findMax(int[] array,int num_threads) {
        if (array.length == 0) {
            return 0;
        }

        int max = Integer.MIN_VALUE;
        int chunkSize = array.length / num_threads;  // Size of each chunk

        // Create a list to store the threads
        List<Thread> threads = new ArrayList<>();

        // Create and start the threads
        for (int i = 0; i < num_threads; i++) {
            int start = i * chunkSize;
            int end = (i + 1) * chunkSize;
            if (i == num_threads - 1) {
                end = array.length;  // Last chunk may be larger
            }
            threads.add(new Thread(new MaxTask(array, start, end)));
            threads.get(i).start();
        }

        // Wait for all threads to complete and get the maximum values
        for (Thread thread : threads) {
            try {
                thread.join();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
        for (int partialMax : MaxTask.getPartialMaxes()) {
            max = Math.max(max, partialMax);
        }

        return max;
    }
    public static void main(String[]args){
        int[] array= {9,45,6,7,87,32,5,23,54,65,76,3,2,5456,2321,545,56,322,121,657,3,2365,623,5423,325,65,23,546,2,54,21,65,73,46,5,232,665,6,3242,6544,213,645,5345};
        int max = findMax(array,4);
        System.out.println(max);
    }
}

class MaxTask implements Runnable {
    private static final List<Integer> partialMaxes = new ArrayList<>();  // List to store partial maxes

    private final int[] array;  // Array to search
    private final int start;    // Start of range
    private final int end;      // End of range

    public MaxTask(int[] array, int start, int end) {
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

