package algorithm.sorting;

import java.util.Arrays;
import java.util.Random;

public class InsertionSort {

	public static void doSort() {
		int t;
		int[] a = new int[15];

		for (int i = 0; i < a.length; i++) {
			a[i] = new Random().nextInt(100);
		}
		System.out.println("Before sorting\t" + Arrays.toString(a));
		
		for(int i=1;i<a.length;i++) {
			int te=a[i];
			t=i-1;
			while(t>=0 && te<a[t]) {
				a[t+1]=a[t];
				t-=1;
			}
			a[t+1]=te;					
		}
		System.out.println("After sorting as ascending\t" + Arrays.toString(a));


		for(int i=1;i<a.length;i++) {
			int te=a[i];
			t=i-1;
			while(t>=0 && te>a[t]) {
				a[t+1]=a[t];
				t-=1;
			}
			a[t+1]=te;					
		}
		System.out.println("After sorting as descending\t" + Arrays.toString(a));
	}
}
