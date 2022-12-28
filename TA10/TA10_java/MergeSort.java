package TA10_java;

import java.util.Arrays;

public class MergeSort {
    public static void mergeSort(int[] array) {
        if (array.length > 1) {
            int mid = array.length / 2;

            // Split the array into left and right halves
            int[] left = Arrays.copyOfRange(array, 0, mid);
            int[] right = Arrays.copyOfRange(array, mid, array.length);

            // Sort the left and right halves in parallel
            Thread t1 = new Thread(() -> mergeSort(left));
            Thread t2 = new Thread(() -> mergeSort(right));
            t1.start();
            t2.start();

            // Wait for both threads to complete
            try {
                t1.join();
                t2.join();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }

            // Merge the sorted halves
            merge(array, left, right);
        }
    }

    public static void merge(int[] array, int[] left, int[] right) {
        int i = 0, j = 0, k = 0;
        while (i < left.length && j < right.length) {
            if (left[i] < right[j]) {
                array[k] = left[i];
                i++;
            } else {
                array[k] = right[j];
                j++;
            }
            k++;
        }

        // Copy any remaining elements from the left or right arrays
        while (i < left.length) {
            array[k] = left[i];
            i++;
            k++;
        }
        while (j < right.length) {
            array[k] = right[j];
            j++;
            k++;
        }
    }

    public static void main(String[] args) {
        int[] array = {3, 7, 8, 5, 2, 1, 9, 5, 4};
        mergeSort(array);
        System.out.println(Arrays.toString(array));  // [1, 2, 3, 4, 5, 5, 7, 8, 9]
    }
}
