package TA10_java;

import java.util.ArrayList;
import java.util.List;

public class SumTask implements Runnable {
    private static final List<Long> partialSums = new ArrayList<>();  // List to store partial sums

    private final int start;  // Start of range
    private final int end;    // End of range

    public SumTask(int start, int end) {
        this.start = start;
        this.end = end;
    }

    @Override
    public void run() {
        long sum = 0;
        for (int i = start; i <= end; i++) {
            sum += i;
        }
        partialSums.add(sum);  // Add partial sum to list
    }

    public static List<Long> getPartialSums() {
        return partialSums;
    }
}